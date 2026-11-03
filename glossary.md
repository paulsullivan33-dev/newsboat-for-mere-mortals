# Glossary

**Article / item.** One entry in a feed:
a title, a date, a body of text, and the
link it came from. "Article" is the
reader's word; "item" is the feed format's
(and the cache table's: `rss_item`).

**Atom.** One of the two feed formats.
XML, standardised, and the dialect the
lab's kitchen journal speaks. Newsboat
reads Atom and RSS through the same code
path; the difference is the publisher's
choice, not yours.

**Bookmark command (`bookmark-cmd`).**
Your own program, named in the config,
that Newsboat calls with an article's
address, title, description and feed
title when you press `Ctrl-B`. Newsboat
keeps no bookmarks itself.

**Browser (setting).** The config string
Newsboat runs when you open an article's
page — anything from `firefox` to a
script; `%u` in the string is where the
address goes.

**Cache.** Newsboat's SQLite database
(`cache.db`): every fetched feed and
article, plus read state, flags and
enclosures. The program's whole memory in
one file you can inspect with `sqlite3`.

**Cleanup-on-quit.** Config setting,
default yes: on exit, delete the cached
data of feeds no longer in the urls file.
Not the read-article setting — that is
`delete-read-articles-on-quit`, which
flags rows `deleted = 1` instead of
removing them.

**Enclosure.** A file attached to a feed
item by address, size and type — for
podcasts, the episode's audio. Pressing
`e` queues it for Podboat.

**Feed.** A site's published list of its
newest articles (RSS or Atom) — and, by
extension, the line in your urls file
that follows it, and its row of counts in
the feed list.

**Feed list.** Newsboat's opening screen:
your feeds, each with an `N` while it
holds anything unread and an
`(unread/total)` pair. Its header counts
feeds, not articles.

**Filter language.** The small grammar
for conditions on articles —
`unread = "yes"`, `feedtitle =~ "Garden"`,
joined with `and`/`or` — used by searches
and query feeds.

**Macro.** Config lines that chain
operations behind one key, run by
pressing `,` then the key, as in
`macro R mark-all-feeds-read`.

**`max-items`.** Config setting capping
each feed at that many newest articles in
the cache; older ones are never kept.

**OPML.** The outline format every feed
reader imports and exports: subscriptions
as XML. Newsboat's plain export drops
tags; `--export-to-opml2` keeps them as
categories.

**Podboat.** Newsboat's companion
program: reads the queue file, downloads
the enclosures you queued, and marks them
`downloaded` in the same file.

**Query feed.** A feed defined by a
filter instead of an address
(`"query:Name:filter"` in the urls file).
It is answered from the cache each time
it is opened, so articles that stop
matching simply leave it — and it shows
`(0/0)` in the feed list regardless.

**Read state.** The per-article flag that
decides the `N`, the counts, and what
`print-unread` reports. Set the moment an
article is opened; toggled back with `N`
in the article list.

**Reload.** Fetching feeds again. `r`
reloads one feed, `R` all of them, and
`newsboat -x reload` does it and exits —
the scriptable form.

**RSS.** The older, looser feed format
family; the lab's garden journal speaks
RSS 2.0. See **Atom** for the other
dialect.

**Tag.** A quoted label after a feed's
address in the urls file. Folders from an
imported OPML arrive as tags.

**urls file.** `~/.newsboat/urls`: one
feed address per line, with optional
tags — the entire subscription database,
kept as text you can edit and back up.
