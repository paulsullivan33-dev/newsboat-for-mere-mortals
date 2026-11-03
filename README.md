# Newsboat for Mere Mortals

Websites publish **feeds** — machine-readable
lists of their newest articles — and a feed
reader collects those lists in one place, so
you can read twenty sites without visiting
twenty sites. **Newsboat** is a feed reader
that lives entirely in a terminal: a keyboard
interface, a subscriptions file you can read
with your own eyes, and a single database file
holding everything it has fetched. No account,
no service in the middle, nothing to sync
unless you carry the files yourself.

This guide explains how Newsboat fits
together, how to get it (including the awkward
case of a system whose package collection
dropped it, which the lab met head-on), and
how to use it properly: subscribing, reading,
searching, filtering with query feeds, handing
articles to a browser or a bookmark script,
and queueing podcast episodes for its
companion program **Podboat**.

The lab behind this guide ran the real thing:
**Newsboat 2.34.1**, built from the project's
own release tarball after the lab's Ubuntu
24.04 machine turned out to carry no Newsboat
package at all — chapter 3 tells that story
with the receipts. It read three invented
fixture feeds served from the lab's own
machine (a gardening journal in RSS, a kitchen
journal in Atom, and a small podcast), plus
one real public feed — the project's own
release feed — to prove the same commands work
out on the internet. It searched, filtered,
imported and exported OPML, bookmarked through
a script, ran a macro, capped a feed at three
articles, cleaned the cache two different
ways, downloaded a podcast episode with
Podboat, and fed Newsboat a broken feed and a
missing one to see what it would say. The
failures are in the transcripts too.

What the lab could not do, it did not fake.
Newer Newsboat releases need a newer Rust
compiler than the lab machine's distribution
ships, so the build is 2.34.1 rather than the
current 2.45 — chapter 3 shows the evidence
and criteria.md keeps the full ledger. The
feed-server features (reading through FreshRSS
or Miniflux accounts, which Newsboat can do)
are described from the documentation, not run;
this guide's neighbours chapter points at the
guides that cover those servers themselves.

One privacy note belongs up front, because it
shapes how to use the tool well. Newsboat
keeps a faithful record of your reading: which
articles arrived, which you opened, which you
saved or bookmarked — all in one database file
on your disk. That is what makes it useful,
and it also makes that file a reading diary.
It stays on your machine; guard it the way you
would a browser history. And on the other
side: every reload tells each publisher's
server that someone at your address fetched
the feed, and when. Chapter 1 returns to both
points before any procedure depends on them.

## What this guide covers

- [**What Newsboat is**](what-newsboat-is.md) —
  the mental model: feeds your machine fetches
  itself, a list of articles, the read ones
  fading and the unread ones waiting
- [**The moving parts**](the-moving-parts.md) —
  the urls file, the cache database, the config
  file, the queue file, and the second program,
  Podboat — and which part holds what
- [**Installing Newsboat**](installing-newsboat.md) —
  the package where your distribution has one,
  the gap where it doesn't, and the source build
  the lab actually ran, with versions checked
- [**Your first feeds**](your-first-feeds.md) —
  the subscriptions file, the first reload from
  the command line, and the feed list read
  line by line
- [**Reading articles**](reading-articles.md) —
  opening and reading, what the `N` flag means,
  the moment an article becomes read, and saving
  an article to a file of its own
- [**OPML and tags**](opml-and-tags.md) —
  labelling feeds with tags, and moving a whole
  subscription list in or out with OPML,
  including what the export quietly drops
- [**Searching and query feeds**](searching-and-query-feeds.md) —
  the slash search, the filter language, and
  feeds that are really standing questions
- [**The browser and bookmarks**](browser-and-bookmarks.md) —
  handing an article to a real browser, and
  bookmarking as a contract with a script
  you own
- [**Podcasts with Podboat**](podcasts-with-podboat.md) —
  the queue file that joins the two programs,
  and an episode downloaded end to end
- [**Configuration and housekeeping**](configuration-and-housekeeping.md) —
  the config file, macros that chain commands,
  `max-items`, and the two cleanups that are
  easy to confuse
- [**Recipes**](recipes.md) — a morning
  unread check from cron, one feed for several
  topics, an OPML backup habit, and a
  tidy-cache routine
- [**The neighbours**](the-neighbours.md) —
  FreshRSS and Miniflux on a server, Liferea
  on the desktop, and the hosted readers: what
  each does that Newsboat doesn't, and vice
  versa
- [**Limits**](limits.md) — no sync of its
  own, one machine's reading diary, silent
  failures on the command line, and feeds that
  can simply stop
- [**Troubleshooting**](troubleshooting.md) —
  the feed that shows a raw URL, the empty
  feed error, the config command Newsboat
  refuses, and the traps this guide's lab
  fell into
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Running Newsboat against a feed server
account (FreshRSS, Miniflux, Nextcloud News
and friends are configuration the project
documents; the lab read plain feeds only, and
the neighbours chapter points to the server
guides). Feed *writing* — publishing your own
RSS or Atom — is the other direction entirely
and belongs to the tools that generate sites.
Reading mail or Usenet in the terminal is a
different pair of tools with their own guides.
And this is not a guide to the fixture feeds'
subjects: the gardening and kitchen articles
are invented stand-ins, there to be read by
the software, not followed in a real garden.

## How to use this guide

Read chapter 1 for the model, and chapter 2
before installing anything — knowing which
file holds what turns later confusion into a
named problem. Chapters 3 and 4 get you a
program and your first feeds; chapter 5 has
you reading in the same sitting. Chapter 7 is
the one to read slowly: query feeds are where
Newsboat stops being a mailbox and starts
being a filter you design. The lab's
transcripts live in `newsboat-lab/transcripts/`;
its fixture feeds, the pages they link to, and
the small scripts it used are beside them in
`newsboat-lab/`, so every claim can be re-run,
not just read.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [FreshRSS for Mere Mortals](https://paulsullivan33-dev.github.io/freshrss-for-mere-mortals/)
- [Miniflux for Mere Mortals](https://paulsullivan33-dev.github.io/miniflux-for-mere-mortals/)
- [tmux for Mere Mortals](https://paulsullivan33-dev.github.io/tmux-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/newsboat-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/newsboat-for-mere-mortals/blob/main/LICENSE-CODE).
