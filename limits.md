# Limits

Outcome: a clear-eyed list of what
Newsboat will not do, so none of it
surprises you mid-habit.

**One machine's reading.** There is no
built-in sync. Your read state lives in
one cache on one machine; a second
machine has a second cache, and the two
will disagree by lunchtime. The escapes
are a feed server behind Newsboat
(chapter 12) or carrying the `~/.newsboat`
directory yourself — both real, neither
automatic.

**It renders what the feed carries.** A
feed that publishes only headlines gives
you headlines; one that publishes stubs
gives stubs, and the article lives behind
the browser key. Newsboat does not fetch
and extract full pages on its own, and
its text view shows the feed's text, with
the feed's idea of formatting.

**Feeds fail quietly from the command
line.** The lab's broken and missing
feeds: `newsboat -x reload` exited 0 in
silence, loaded the healthy feed, and
left the failures to be discovered in
the interface — an empty feed with its
channel title, a raw URL where the 404
feed's title never arrived, and "Error:
feed contains no items!" on opening one.
Scheduled reloads therefore fail
*gracefully and invisibly*; check counts
(`print-unread`) or the cache if a feed
matters.

**Reading is marked at the door.** An
article becomes read when opened, not
when finished (chapter 5). There is no
half-read state, and the rescue is manual
(`N` in the article list toggles an
article's read status back), not a
workflow.

**The cache's words are slippery.**
"Cleanup" and "delete" name at least
three different operations (chapter 10),
one of which only flags rows in the
database. Anyone administering the cache
file by its size will be misled unless
they know about the flag.

**Counts have a blind spot.** Query
feeds show `(0/0)` in the feed list no
matter what they contain. Anything —
script or habit — that reads the feed
list for "is there anything to read"
must treat query feeds separately.

**It is a reader, not an archive.**
Articles leave feeds; feeds end; sites
die. What you did not save (chapter 5) or
enqueue (chapter 9) can become
unrecoverable on someone else's schedule,
not yours. Newsboat keeps what it
fetched under your cleanup rules — no
more.

**The interface is a terminal's.** No
images inline, no touch, no phone. For
some readers that is the feature; for
others the limit. Chapter 12 is the map
of where those readers go.
