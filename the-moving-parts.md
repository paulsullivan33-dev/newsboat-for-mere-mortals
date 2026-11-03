# The Moving Parts

Outcome: you can name every file Newsboat
keeps, say which part of the program reads
it, and predict where a change will show
up. When something surprises you later,
this chapter is the map.

Newsboat keeps its whole life in one
directory — `~/.newsboat/` by default, or
`~/.config/newsboat/` if you use the XDG
layout. The lab's `--help` output lists
the three that matter most:

```text
Files:
    - configuration:  ~/.newsboat/config
    - feed URLs:      ~/.newsboat/urls
    - cache:          ~/.newsboat/cache.db
```

## The urls file: what you follow

`urls` is a plain text file, one feed per
line, in the order you want them listed.
After the address you may add **tags** —
quoted words that label the feed:

```text
http://127.0.0.1:18089/feeds/garden-notes.xml "Garden and Kitchen" garden
```

That is the entire subscription database.
You can edit it with any editor, keep it
in a backup, or rebuild it by importing an
OPML file (chapter 6). Newsboat itself
never hides it from you: when this guide
says "subscribe", it means "add a line to
this file".

## The cache: what it fetched and what you did

`cache.db` is a SQLite database — an
ordinary file in the most ordinary database
format there is. It holds two tables that
matter: `rss_feed` (one row per feed) and
`rss_item` (one row per article). Each
article row carries its title, its text,
its date — and its **read state**, the
little flag that decides whether the
article list shows an `N`.

You can look inside whenever you like,
which this guide does repeatedly, because
it turns "Newsboat feels like it lost an
article" into a question with an answer:

```text
$ sqlite3 ~/.newsboat/cache.db "SELECT count(*) FROM rss_item;"
14
```

Deleting the cache is not a
subscription-ending disaster: the feeds
are re-fetched from the urls file on the
next reload, and only the reading history
is lost. Chapter 10 is about what leaves
the cache on purpose.

## The config file: how it behaves

`config` is another plain text file, one
setting per line — `browser "w3m %u"`,
`max-items 3`, and so on. It is optional:
Newsboat starts happily without one, and
everything in this guide before chapter 8
used defaults. Two warnings from the lab.
Newsboat is strict: an unknown setting is
refused at startup, in plain words —

```text
Loading configuration...unknown command `bookmark-autosave'
```

— and there is no "mostly loaded" state to
limp along in. And because the file is
parsed fresh at every start, editing it
needs no restart ritual; quit, edit,
start again.

## The queue file: where the two programs meet

Podcasts introduce a fourth file, `queue`,
in the same directory. When you press `e`
on an article with an audio enclosure,
Newsboat appends one line: the episode's
address, the file it should become, and
later its status. **Podboat**, the second
program, reads the same file and does the
downloading. Neither program talks to the
other directly; the file is the whole
contract, and chapter 9 reads it line by
line.

## The parts that are not files

Three pieces of machinery tie the files
together. The **fetcher and parser** speak
HTTP through libcurl and read RSS and Atom
through libxml2 — the two feed dialects
are one code path by the time an article
exists. The **filter language** is a small
query grammar (`unread = "yes"`,
`feedtitle =~ "Garden"`) used by searches
and query feeds (chapter 7). And the
**interface** is a stack of full-screen
lists — feeds, then articles, then one
article — drawn by a forms library, with
`q` always stepping one level back and
`?` always showing the keys for the level
you are in.

Check: run `newsboat --help` and find the
three file paths at the bottom. Everything
in this guide happens inside those paths.
