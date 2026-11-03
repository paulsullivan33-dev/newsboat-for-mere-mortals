# Your First Feeds

Outcome: a subscriptions file with three
feeds in it, a first reload, and a feed
list you can read at a glance. The lab's
feeds come from its own fixture server;
yours will be real addresses, and every
step is identical.

## Writing the urls file

Create `~/.newsboat/urls` with one feed
address per line. The lab's file points
at three feeds on its own machine — an
RSS gardening journal, an Atom kitchen
journal, and a podcast:

```text
http://127.0.0.1:18089/feeds/garden-notes.xml "Garden and Kitchen" garden
http://127.0.0.1:18089/feeds/kitchen-journal.xml "Garden and Kitchen" kitchen
http://127.0.0.1:18089/feeds/workshop-podcast.xml "Listening" podcast
```

The quoted words are tags, labels you
choose; chapter 6 gives them their own
chapter. For a first run, bare addresses
are enough — most sites publish their feed
address in the page footer or behind the
orange RSS icon, and pasting it here is
the whole subscription ceremony.

## The first reload, without the interface

Newsboat can fetch from the command line,
which is both a fine first test and the
form scripts and cron jobs use later:

```text
$ newsboat -x reload print-unread
14 unread articles
```

`-x` runs commands and exits: `reload`
fetched all three feeds, `print-unread`
counted the new articles. Fourteen is
right, and the cache proves it another
way (chapter 2's map, used for real):

```text
$ sqlite3 ~/.newsboat/cache.db \
    "SELECT title, (SELECT count(*) FROM rss_item
      WHERE feedurl = rss_feed.rssurl) FROM rss_feed;"
The Example Garden Notes|8
The Sample Kitchen Journal|4
The Workshop Bench Podcast|2
```

Eight plus four plus two: what the feeds
published is what the cache holds.

## The feed list

Now open the program itself — type
`newsboat`:

```text
Newsboat 2.34.1 - Your feeds (3 unread, 3 total)
>>    1 N       (8/8) The Example Garden Notes
      2 N       (4/4) The Sample Kitchen Journal
      3 N       (2/2) The Workshop Bench Podcast

q:Quit ENTER:Open n:Next Unread r:Reload R:Reload All A:Mark Read C:Mark All Read /:Search ?:Help
```

Read it in pieces. The title counts
**feeds**, not articles: "3 unread, 3
total" means all three feeds contain
something unread. Each line carries the
feed's number; an `N` while it holds
anything unread; the pair `(unread/total)`
for that feed; and its title — the title
the *feed itself* declares, not the file
name you subscribed to. The `>>` marks
the selected line (this guide's
transcripts add it; on your screen the
selection is the highlighted row). The
bottom line is the level's key map:
`q` quits (and from deeper levels, steps
back), Enter opens, `r` reloads the
selected feed, `R` reloads them all, and
`?` shows the full key list for where you
are standing.

Two habits start here. Pressing `R`
before reading means the list you work
through is current. And the `(unread/total)`
pair is the whole triage: a feed at
`(0/24)` is a feed you are on top of.

Check: your header count of unread feeds,
and the per-feed pairs, agree with what
`print-unread` said from the command
line — the interface and the database
never disagree, because the interface is
a view of the database.
