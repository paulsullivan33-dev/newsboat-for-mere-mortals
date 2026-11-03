# Recipes

Outcome: a handful of complete, small
jobs, each assembled from pieces the
earlier chapters proved.

## A morning unread count, without opening anything

Because reload works from the command
line (chapter 4), cron can fetch before
you wake, and a one-line check can be
your door into the morning:

```bash
newsboat -x reload print-unread
# 14 unread articles
```

Run the reload an hour early from cron;
run just `print-unread` yourself when you
sit down. If the number is boring, the
morning is yours; if it is not, the
interface is one word away. (The lab ran
the command form throughout; the cron
line itself is the same command on a
schedule.)

## One inbox for a topic, from several feeds

You follow three sites for one subject
and want them as one stream. Give them a
shared tag in the urls file, then a query
feed that selects by that tag's feeds —
or, as the lab did, by feed title
pattern:

```text
"query:Unread garden notes:unread = \"yes\" and feedtitle =~ \"Garden\""
```

Read from the query feed; it empties as
you go (chapter 7). Keep the real feeds
below it for the days you want one site
at a time. This is the recipe the query
chapter exists for: the inbox is a
question, and it re-asks itself at every
open.

## The standing OPML backup

Your subscriptions are one text file,
but the OPML export is the form every
other reader accepts — keep both fresh
with a weekly habit:

```bash
cp ~/.newsboat/urls ~/backups/newsboat-urls-$(date +%F)
newsboat --export-to-opml2 > ~/backups/newsboat-subs-$(date +%F).opml
```

Use the 2.0 export so the tags ride
along (chapter 6). The urls copy is the
one *you* would restore; the OPML is the
one any successor tool would import.

## Saving the keepers, on purpose

Read an article worth a decade, press
`s`, and give it a deliberate name in a
deliberate folder instead of accepting
the suggested one (chapter 5's dialog is
a real file dialog; navigate it). Saved
articles are outside every cache rule in
chapter 10, so a yearly folder of them —
`~/reading/2026/` — becomes an archive
that no cleanup can surprise. Pair with
the bookmark script (chapter 8) when
what you want to keep is the *address*
rather than the text.

## The podcast queue as a shopping list

Queue episodes all week with `e` — from
article lists, from a query feed of
unread podcast items — and let Podboat
drain the queue when you say so (chapter
9), or flip its automatic download toggle
(`a`) once and let it drain itself at
each start. Because the queue is a text
file, an episode can also be added by
hand or by script: one line, address and
target path, and Podboat treats it as its
own.

## A pre-holiday tidy

Before a trip (or a backup), in order:
`R` inside Newsboat to fetch everything;
read or mark-read the backlog with the
`,R`-style macro (chapter 10); quit, so
`cleanup-on-quit` drops anything
unsubscribed; then `newsboat --vacuum`
once, for luck. The cache you carry is
the cache you meant to have.
