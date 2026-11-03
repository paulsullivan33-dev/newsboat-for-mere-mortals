# Configuration and Housekeeping

Outcome: your Newsboat behaves the way you
told it to — browser, bookmarks, a macro
of your own — and its cache stays a size
you chose, by rules you can state.

## The config file, briefly

`~/.newsboat/config`, one setting per
line, read at every start. This guide has
already used four real ones:

```text
browser "/path/to/show-url.sh %u"
bookmark-cmd "/path/to/bookmark.sh"
download-path "/home/you/downloads"
max-items 3
```

The manual lists a hundred more —
colours, formats, key bindings
(`bind-key`), the external editor for
composing, feed-sort orders. Those are
documented-only here; the lab ran the
ones above and the two cleanups below,
and one rule the lab learned by falling
over it applies to all: **a setting
Newsboat does not know stops the start**,
with the setting named (`unknown command
'bookmark-autosave'` was the lab's own
invention being refused). Check spelling
against the manual before blaming the
file — a refused config leaves Newsboat
unstarted, not half-configured.

## Macros: keys that do several things

A **macro** chains operations behind one
key, invoked by pressing `,` then the
key. The lab's was a tidy-up:

```text
macro R mark-all-feeds-read
```

With feeds at `(2/8)`, `(4/4)` and `(2/2)`,
`,R` ran the operation — including its
built-in conscience:

```text
Do you really want to mark all feeds as read (y:Yes n:No)?
```

— and after `y`, the list read `(0/8)`,
`(0/4)`, `(0/2)` and `print-unread`
outside agreed: `0 unread articles`.
Macros can chain several operations with
`;` (the classic example opens an article
in a chosen browser by setting `browser`
first, then opening). The operations
available are the same ones keys bind to;
`?` and the manual's operation table are
the catalogue. Keep macros few and named
by what they finish, not what they press.

## Housekeeping: three different bins

The cache only grows unless you rule it.
Newsboat offers three separate controls,
and the lab's most useful hour was spent
disentangling them — two have similar
names and do different jobs.

**`max-items N`** caps each feed at its N
newest articles, enforced as feeds load.
Same 8-article garden feed, unlimited
cache: 8 rows. Fresh cache with
`max-items 3`: 3 rows — and reading them
shows the three are the *newest* three
(tomatoes, compost, seedlings). The older
five are not hidden; they were never
kept. This is the control for noisy feeds
you dip into rather than finish.

**`cleanup-on-quit`** (default: **yes**)
deletes the data of feeds that are *no
longer in your urls file*, each time
Newsboat closes. The lab copied its main
setup, cut the podcast line from the
copy's urls, opened and quit: the item
count went **14 → 12** and the feed rows
**3 → 2**, with no prompt — unsubscribing
really does take the archive with it.
The same job on demand is the
`--cleanup` flag, which took the lab's
OPML test cache from 12 items to 8 when
pointed at a garden-only urls file.

**`delete-read-articles-on-quit`**
(default: no) is the one whose name
promises the most and delivers the least,
literally: it does not delete rows. It
*flags* read articles `deleted = 1` in
the database. On the lab's all-read copy,
one open-and-quit left 14 rows — all 14
flagged — and reopening showed every feed
at `(0/0)`: invisible, uncounted, and
still occupying the file until a
`cleanup-on-quit` or a feed's departure
removes them for real. (The lab confirmed
the flag in the source before believing
its own count.) If your cache file seems
too big for the reading it shows, this
flag is one reason why; `newsboat
--vacuum` (SQL-level compaction) is the
documented companion step.

Set one rule per intention — cap the
noisy, let unsubscribe mean unsubscribe,
and know that "deleted" can mean
"flagged" — and the cache stays a tool
instead of a sediment.

Check: with a scratch setup, reload an
8-article feed under `max-items 3` and
count rows with `sqlite3`; the answer
must be 3, and the titles must be the
three newest.
