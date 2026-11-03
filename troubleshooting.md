# Troubleshooting

Outcome: the failures name themselves,
and each has a check that separates "the
tool is broken" from "the tool is telling
you something".

## A feed shows its raw URL instead of a title

The feed never delivered a parseable
document — the address is wrong, the
server returned an error page, or the
feed moved. Check from outside the
interface first:

```bash
curl -sI http://example.com/feed.xml | head -1
curl -s http://example.com/feed.xml | head -5
```

An HTML `<!DOCTYPE...>` in the second
command means the "feed" is a web page.
The lab's 404 fixture produced exactly
this symptom: raw URL, `(0/0)`, forever.

## A feed loads but shows (0/0), and opening it says "Error: feed contains no items!"

The document arrived and its channel
information parsed, but no items
survived: the XML is malformed below the
channel (the lab's broken fixture, whose
channel never closes), or the feed is
genuinely empty. Validate the document
itself:

```bash
curl -s http://example.com/feed.xml | xmllint - > /dev/null
```

A parser error there is the feed's
fault, and no reader setting will fix it.

## Newsboat refuses to start: "unknown command"

A config line it does not know — the
lab's self-inflicted case was
`bookmark-autosave`, a setting invented
from wishful thinking. The message names
the command; the manual's configuration
table has the real names. Comment the
line out, start, and check the spelling
before re-enabling it. Newsboat does not
offer a degraded start, so this failure
is total but always announced.

## The macro did nothing

Three usual causes: the macro is bound
in config but invoked without the leading
comma (`,` then the key); the operation
name is misspelled (config lets an
unknown operation pass more quietly than
an unknown setting — check against `?`
and the operations table); or the
operation itself asked a question, as
`mark-all-feeds-read` does, and the
confirmation is waiting at the bottom of
the screen.

## Arrow keys do not move the selection

Seen on unusual terminals: Newsboat's
interface library speaks the terminal's
*application* cursor mode. If arrows are
dead but letters work, try `j`/`k` where
bound, and check `TERM` is set to your
terminal's real entry — a wrong `TERM`
breaks the keys before it breaks the
colours. (The lab's recorder hit this
from the other side: sending plain ANSI
arrows to the application-mode program
left the selection frozen, which is how
the guide's transcript driver learned to
send the application-mode sequences.)

## The browser opens and Newsboat seems hung

It is waiting: Newsboat runs the browser
command and resumes when it exits. A
graphical browser that hands off to an
already-running instance returns at once,
which looks like nothing happened; one
that stays resident holds Newsboat until
it closes. The check is the command
itself — run the same string in a shell
with the article's address in place of
`%u`.

## Podboat shows the episode as "queued" forever

That is its resting state, not a stall:
press `d` on the entry, or enable
automatic download with `a`. If `d`
fails, the two things to verify are the
queue file (does the line carry the right
address?) and `download-path` (does the
folder exist and accept writes?). The
queue line gains the word `downloaded`
only on success.

## The cache is bigger than the reading it shows

Read articles flagged `deleted = 1`
(chapter 10) still occupy rows. Look
before you prune:

```bash
sqlite3 ~/.newsboat/cache.db \
  "SELECT count(*) FROM rss_item WHERE deleted = 1;"
```

`--cleanup` removes unsubscribed feeds'
data for real; `--vacuum` compacts the
file afterwards.
