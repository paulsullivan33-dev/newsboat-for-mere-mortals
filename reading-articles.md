# Reading Articles

Outcome: you can work through a feed the
way Newsboat intends — open, read, move on
— and you know exactly when an article
becomes "read", plus how to keep one
forever as a file.

## The article list

Enter on a feed opens its articles,
newest first:

```text
Newsboat 2.34.1 - Articles in feed 'The Example Garden Notes' (8 unread, 8 total)
>>    1 N  Oct 30   257   Watering tomatoes without drowning them
      2 N  Oct 28   208   Compost: the three-bin habit
      3 N  Oct 26   225   Why seedlings lean toward the window
      ...
      8 N  Oct 14   188   The case for a small garden
```

Each line: the article's number, the `N`
for unread, its date, a size (the column
of numbers — the article's length in
characters), and its title. This header
counts **articles**, where the feed list
counted feeds; "(8 unread, 8 total)" is
this feed's share of your morning.

One behaviour to expect: when you return
to a feed, the selection starts on the
first *unread* article, not the first
article — Newsboat assumes you are
continuing, not starting over.

## Reading, and the moment of reading

Enter opens the article as plain text,
with a small header — feed, title, date,
and the link it came from:

```text
Feed: The Example Garden Notes
Title: Watering tomatoes without drowning them
Date: Fri, 30 Oct 2026 08:00:00 +0000
Link: http://127.0.0.1:18089/garden/watering-tomatoes.html

Tomatoes like a deep drink twice a week, not a shallow sip every day. ...
```

Watch the title bar: it already says
"(7 unread, 8 total)". **Opening an
article marks it read — immediately, not
when you finish it, and not when you
close it.** Back in the list, the article
has lost its `N`; back in the feed list,
the garden feed reads `(7/8)`. That is
the whole read-state machine: there is no
"mark as read" step to remember, and —
the edge of the same knife — a mis-tap
that opens an article marks it too. `n`
in the article view walks to the next
unread article, which is the fast way
through a long feed; `Ctrl-N` and the
article-list `A` key (mark all read) are
how a feed you have skimmed gets cleared
without opening twenty articles. Newsboat
asks before that last one acts, as it
does before anything destructive: "Do you
really want to mark all feeds as read
(y:Yes n:No)?" appeared in the macro
transcript (chapter 10) for the same
operation.

The `~` lines filling the bottom of a
short article are just padding — the
article viewer's way of showing empty
space, like a text editor's.

## Saving an article to keep

Reading is fleeting by design (chapter 10
deletes read articles by rules); saving is
how an article escapes. Press `s` in the
article or the list, and Newsboat offers
a save dialog with a name it builds from
the title:

```text
Newsboat 2.34.1 - Save File - /home/you
File: Watering_tomatoes_without_drowning_them.txt
ESC,q:Cancel ENTER:Save
```

Accept the name, or edit it — it is a
real file dialog with the current
directory listed, not a bare prompt, so
type carefully: the lab once typed its
chosen name *after* the suggested one and
saved a file under the two names joined
together. Saving writes the article's
text, headers included:

```text
Saved article to Watering_tomatoes_without_drowning_them.txt.
```

A saved article is yours outside the
cache's rules — a plain file in a folder
of your choosing, which recipes in
chapter 11 build on.

Check: after reading one article, the
three counts (article header, article
list, feed list) all step down by one,
together, and `newsboat -x print-unread`
outside the interface agrees.
