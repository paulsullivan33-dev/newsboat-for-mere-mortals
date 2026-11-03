#!/usr/bin/env python3
"""Drive a Newsboat TUI session under a pty and record clean transcripts.

Usage: drive.py SESSION_FILE OUTFILE

The session file has one step per line:
  # comment
  CMD <argv...>        first line: the command to spawn
  SAY  text            narration line printed into the transcript
  SEND text            (\\n \\t \\e are decoded; ^X means control-X)
  SENDKEY enter|up|down|space|esc
  WAIT seconds
  SNAP label           render the current terminal screen (via a real
                       terminal emulator, pyte) into the transcript

The child's environment is the caller's; set HOME and TERM before
calling so Newsboat uses the lab's scratch home directory.
"""
import os
import sys
import time

import pexpect
import pyte

COLS, ROWS = 120, 40


def decode(s):
    out = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            nxt = s[i + 1]
            out += {"n": "\n", "t": "\t", "e": "\x1b", "\\": "\\"}.get(nxt, nxt)
            i += 2
        elif c == "^" and i + 1 < len(s):
            out += chr(ord(s[i + 1].upper()) - 64)
            i += 2
        else:
            out += c
            i += 1
    return out


def main():
    session_file, outfile = sys.argv[1], sys.argv[2]
    steps = open(session_file).read().splitlines()
    cmd = None
    for ln in steps:
        if ln.startswith("CMD "):
            cmd = ln[4:].strip()
            break
    if not cmd:
        sys.exit("session file needs a CMD line")

    screen = pyte.Screen(COLS, ROWS)
    stream = pyte.ByteStream(screen)
    child = pexpect.spawn(cmd, env=os.environ, encoding=None, timeout=30,
                          dimensions=(ROWS, COLS))
    transcript = []

    def drain(wait=0.6):
        end = time.time() + wait
        while time.time() < end:
            try:
                chunk = child.read_nonblocking(size=65536, timeout=0.2)
                if chunk:
                    try:
                        stream.feed(chunk)
                    except Exception:
                        pass  # an escape the emulator can't do; keep going
                    end = time.time() + 0.35  # extend while data flows
            except (pexpect.TIMEOUT, pexpect.EOF):
                break

    drain(1.5)
    for ln in steps:
        if not ln or ln.startswith("#") or ln.startswith("CMD "):
            continue
        if ln.startswith("SAY "):
            transcript.append("\n### " + ln[4:])
        elif ln.startswith("SEND "):
            child.send(decode(ln[5:]))
            drain(0.8)
        elif ln.startswith("SENDKEY "):
            key = ln[8:].strip()
            # STFL (Newsboat's form library) runs the terminal in
            # application cursor mode, so arrows are ESC O A/B, not
            # the ANSI ESC [ A/B -- the lab learned this by watching
            # the selection refuse to move.
            child.send({"enter": "\r", "up": "\x1bOA", "down": "\x1bOB",
                        "space": " ", "esc": "\x1b"}[key])
            drain(0.8)
        elif ln.startswith("WAIT "):
            time.sleep(float(ln[5:]))
            drain(0.3)
        elif ln.startswith("SNAP "):
            drain(0.5)
            transcript.append("\n--- screen: " + ln[5:] + " ---")
            lines = []
            for row, text in enumerate(screen.display):
                text = text.rstrip()
                cells = screen.buffer.get(row, {})
                # Newsboat draws the selected list row brown on blue
                # (the title bar and the bottom help line share the
                # colours, so skip the first and last rows).
                cursor_line = (0 < row < ROWS - 1
                               and not text.startswith("q:Quit")) and any(
                    cells[c].bg == "blue" for c in cells
                    if cells[c].data.strip())
                lines.append((">> " if cursor_line else "   ") + text
                             if text else text)
            while lines and not lines[-1]:
                lines.pop()
            transcript.append("\n".join(lines))
    try:
        child.send("q")
        drain(0.5)
        child.terminate(force=True)
    except Exception:
        pass
    with open(outfile, "w") as fh:
        fh.write("\n".join(transcript) + "\n")
    print("wrote", outfile)


if __name__ == "__main__":
    main()
