# What Newsboat Is

Keeping up with websites usually means
visiting them: twenty bookmarks, twenty
page designs, twenty sets of banners and
pop-ups, and no record of what you have
already seen. A **feed** turns that around.
A site that offers a feed publishes a small
structured file — its newest articles as a
list of titles, dates, summaries and links —
and software on *your* side collects the
lists. You read the articles in one place,
in one plain layout, and the software
remembers which ones you have read.

**Newsboat is that software, for people who
like the terminal.** It is a feed reader:
you give it a list of feed addresses, it
fetches them, and it presents what arrived
as a list you work through with the
keyboard. Articles open as clean text.
The ones you have read stop shouting; the
ones you have not wait, marked with an `N`.
When an article deserves the full web page,
Newsboat hands it to a browser of your
choosing and takes back the keyboard when
the browser closes. A companion program,
**Podboat**, downloads podcast episodes you
pick while reading.

Everything is local. Your subscriptions are
a plain text file, one feed per line. What
Newsboat has fetched, and everything it
knows about your reading, sits in one
SQLite database file. There is no account,
no server Newsboat answers to, and no
company collecting the list of what you
read. If the program vanished tomorrow,
the text file of subscriptions would still
open in any editor, and most other readers
would import it.

## A first taste

After installing (chapter 3) and writing
two lines into `~/.newsboat/urls`, this is
the whole daily round:

```text
$ newsboat -x reload print-unread
14 unread articles
```

That fetched every feed and counted what
is new. Opening `newsboat` and pressing
Enter twice puts you inside the newest
article; `q` walks back out, level by
level. Chapter 4 starts exactly there.

## What it is not

Newsboat is not a *sync service*: it keeps
your reading on one machine, and making
two machines agree is your job (or a feed
server's — chapter 12). It is not a web
browser: it renders the text a feed
carries, and sends you out to a browser
for anything more. It is not a read-later
archive unless you make it one — old
articles leave the cache by rules you
control (chapter 10), and chapter 13 is
plain about what that means. And it is
not silent company: it does not phone
home, recommend articles, or rank anything
by anything but date. The list is the
list.

## Who it is for

The person who follows twenty small sites
and resents the twenty-first tab. The
terminal dweller who wants the news in
the same window as everything else. The
reader who wants their subscriptions in a
file they can back up, diff, and carry
from machine to machine for a decade.
The podcast listener who wants episodes
as files, not streams. The common thread
is one person, their own machine, and a
reading habit they would like to own.

## The honest catches, up front

Two, and this guide returns to both.
First, the cache database is a diary: it
records what arrived and what you opened,
in one file, in a format anyone with a
copy can read. Keep it as you would a
browser history — it is yours because it
never leaves your disk, and it is worth
guarding for the same reason. Second,
fetching is not invisible to the other
side: each reload tells the publisher's
server your address and the time, the way
any fetch does. Newsboat adds nothing to
that — no tracking, no identifiers beyond
the request itself — but it does not hide
it either. Neither fact stops anyone
reading the news; both are worth knowing
before the habit forms.
