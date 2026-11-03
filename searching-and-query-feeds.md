# Searching and Query Feeds

Outcome: you can find an article you half
remember, and — the real subject of this
chapter — build a feed that is a standing
question, filling itself with whatever
matches and emptying as you read.

## The slash search

Press `/` in the article list (or the
feed list) and type a word. The lab,
standing in the garden feed, searched
`compost`:

```text
Newsboat 2.34.1 - Search results for 'compost' (1 unread, 2 total)
      1    Oct 28   208   |The Example Garde|  Compost: the three-bin habit
>>    2 N  Oct 21   172   |The Example Garde|  Feeding the soil in autumn
```

Two results, and they teach the search's
character. One matched in its *title*;
the other only in its *body* ("a blanket
of compost or leaf mould..."). Search
reads the whole article, not headlines.
The results are an article list like any
other — Enter opens, read state behaves
(`1 unread` because the lab had already
read the compost article), and the extra
`|feed title|` column appears because a
search can reach across feeds. `z`
returns to the previous results if you
search again.

Search is a question you ask once. The
rest of the chapter is asking it forever.

## The filter language

Under the search sits a small language
for talking about articles. Its atoms are
comparisons over an article's fields:

- `unread = "yes"` — the article is unread
  (`"no"` for read); most fields speak in
  strings like this
- `feedtitle =~ "Garden"` — the feed's
  title *matches* the pattern (`=~` is a
  regular-expression match; `=` wants
  exact equality)
- `title =~ "tomato"`, `author = "..."`,
  `date > "2026-10-20"` — other fields
  exist; the lab ran the first two, and
  the manual's table lists them all

Atoms join with `and`, `or`, and
parentheses. The lab's working filter was
one line: `unread = "yes" and feedtitle
=~ "Garden"` — everything unread that the
garden feed published. (The manual's full
field list is documented-only in this
guide, as criteria.md records; the two
atoms above were run for real.)

## Query feeds: a filter wearing a feed's clothes

Put a filter into the urls file, in a
special line, and it becomes a feed:

```text
"query:Unread garden notes:unread = \"yes\" and feedtitle =~ \"Garden\""
```

The format is `"query:` + a name you
invent + `:` + the filter + `"`. In the
feed list it takes its seat like any feed
— third in the lab's test home:

```text
      1 N       (8/8) The Example Garden Notes
      2 N       (4/4) The Sample Kitchen Journal
      3         (0/0) Unread garden notes
```

Note the oddity in plain sight: the query
feed shows `(0/0)` in the list even when
it is full. Query feeds do not report
counts there (the lab watched this
carefully; it is a display gap, not an
empty feed). Open it and the truth
appears, with the feed-title column on,
because a query can span feeds:

```text
Newsboat 2.34.1 - Articles in feed 'Unread garden notes' (8 unread, 8 total) - query:...
>>    1 N  Oct 30   257   |The Example Garde|  Watering tomatoes without drowning them
      ...
```

Then the magic that makes query feeds
worth designing: read the tomato article,
come back, and the same query feed reads
`(7 unread, 7 total)` with the article
*gone from it* — not struck through, gone,
because it no longer matches `unread =
"yes"`. A query feed is a to-do list that
clears itself. Designs that earn their
keep: one for unread across your three
noisiest feeds, one for a word you are
tracking wherever it appears, one for a
single author across several sites.

Nothing is fetched for a query feed; it
is answered from the cache each time you
open it, which is why `R` reloads ignore
it and why its count column stays blank.

Check: write the lab's query line into a
test urls file, read one matching
article, reopen the query feed, and watch
both the count and the list lose it.
