# Podcasts with Podboat

Outcome: a podcast episode goes from a
line in a feed to an audio file on your
disk, through the queue file that joins
Newsboat and Podboat.

## Enclosures: the attachment a feed can carry

Some feed items carry an **enclosure** —
an attached file's address, size, and
type. For podcasts the attachment is the
episode's audio. Newsboat notices
enclosures in two places: the article
view lists them, and one key acts on
them. The lab's podcast feed carries two
episodes, each enclosing a small WAV file
(the lab generated one-second tones; the
machinery cannot tell the difference, and
neither can this chapter's claims).

## Queueing: the `e` key

In the article view — or on an article in
the list — press `e` (enqueue). Nothing
appears to download, and nothing has:
Newsboat appended one line to
`~/.newsboat/queue`:

```text
http://127.0.0.1:18089/audio/episode-02.wav "/home/you/downloads/episode-02.wav"
```

Episode address, then the file it should
become. The folder in the middle is the
`download-path` setting, which both
programs read from the config:

```text
download-path "/home/you/downloads"
```

Leave it unset and downloads land in your
home directory's `~/Downloads`-style
default from the manual; set it once and
both programs agree forever. The queue
file *is* the hand-off — there is no
server, no notification, no shared
memory. Edit it by hand if you like;
Podboat will believe you.

## Downloading: Podboat

Run `podboat` and it reads the queue:

```text
Queue (0 downloads in progress, 1 total) - 0.00 KB/s total
>>    1 [   0.0MB/   0.0MB] [  0.0 %] [   0.00 KB/s] queued    .../episode-02.wav -> /home/you/downloads/...
```

First honest surprise: **queued means
queued** — Podboat does not start on its
own. `d` starts the selected download
(`a` toggles automatic downloading if you
want the queue to drain itself on future
runs). A moment later:

```text
>>    1 [   0.0MB/   0.0MB] [100.0 %] [   1.26 MB/s] ready     .../episode-02.wav -> /home/you/downloads/...
```

And outside the interface, the proof:

```text
$ ls -l downloads/
16044 episode-02.wav
$ file downloads/episode-02.wav
episode-02.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
```

Same byte count the feed promised in its
enclosure `length`, and a real audio
header. The queue line meanwhile gained a
word — it now ends `downloaded` — which
is how both programs remember not to
fetch it again. `P` in Podboat purges
finished entries when the list grows
long; `m` marks one as finished without
downloading (the "already heard it on the
other app" case).

The split is the same philosophy as the
bookmark command: Newsboat is for
choosing, Podboat is for fetching, a
plain file is the contract — and the
episodes end as ordinary audio files in
an ordinary folder, playable by anything,
owned by you.

Check: queue one episode, run Podboat,
press `d`, and compare `ls -l` against
the enclosure size in the feed itself.
