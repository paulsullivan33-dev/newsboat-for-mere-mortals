# OPML and Tags

Outcome: your feeds carry labels you
chose, and you can move the whole list —
in from another reader, or out as a
backup — through OPML, knowing exactly
what survives the trip.

## Tags: the labels in the urls file

A tag is any quoted word after a feed's
address:

```text
http://127.0.0.1:18089/feeds/garden-notes.xml "Garden and Kitchen" garden
http://127.0.0.1:18089/feeds/kitchen-journal.xml "Garden and Kitchen" kitchen
```

A feed can carry several; a tag can span
several feeds. Tags are how a flat list
of thirty feeds gets shape: the feed list
can be narrowed to one tag (press `t` and
pick), and filters and searches can speak
about tags too. In the lab's file both
text feeds share "Garden and Kitchen"
(the section they arrived under) and each
keeps a private one — the shape a real
list grows into on its own.

## OPML in: arriving from another reader

**OPML** is the interchange format every
feed reader speaks: an XML outline of
subscriptions, folders and all. Importing
is one command:

```text
$ newsboat -u setups/opml/urls -c setups/opml/cache.db \
    -i fixtures/opml/fixture.opml
Import of .../fixture.opml finished.
```

(The lab used `-u` and `-c` to keep this
test's files apart from the main setup;
at home, plain `newsboat -i subs.opml`
writes into your real ones.) The fixture
OPML held the two text feeds inside a
folder named "Garden and Kitchen", and
the urls file afterwards shows what an
import does with folders:

```text
http://127.0.0.1:18089/feeds/garden-notes.xml "Garden and Kitchen"
http://127.0.0.1:18089/feeds/kitchen-journal.xml "Garden and Kitchen"
```

The folder became a tag. That is the
general rule of arrival: OPML's folders
flatten into Newsboat's tags, and nothing
else about the old reader survives —
not read state, not settings. A reload
made the import real: `12 unread
articles`, the two feeds working exactly
as if typed by hand.

## OPML out: the backup and the exit door

Export writes OPML to standard output,
so redirect it to keep it:

```text
$ newsboat --export-to-opml > subscriptions.opml
```

What comes out is tidy — feeds with their
titles and site links. But know its one
silence: plain OPML export **drops the
tags**. The lab's round trip proved it:
the exported file has no trace of "Garden
and Kitchen". For a backup that keeps
your labels, use the second form:

```text
$ newsboat --export-to-opml2
```

OPML 2.0 export carries each feed's tags
in a `category` attribute:

```text
<outline type="rss" xmlUrl=".../garden-notes.xml" ... category="Garden and Kitchen,garden"/>
```

So the habits are: `--export-to-opml`
for handing your list to *another
program* (maximum compatibility, labels
left behind), `--export-to-opml2` for
backing up your list for *Newsboat*
(labels kept). Chapter 11 turns the
second into a standing habit.

Check: import a small OPML into a
scratch urls file and diff what you sent
against what the file gained — folders
as tags, addresses intact, in order.
