# The Neighbours

Outcome: you know what to reach for when
Newsboat is not the shape of the job —
and what you would give up by moving.
These tools are characterised from their
documentation and from this series' own
guides, not re-run in this lab.

## FreshRSS — the same reading, on a server

**FreshRSS** is a self-hosted feed
aggregator with a web interface: it lives
on a small server, fetches your feeds
around the clock, and gives every device
a browser view of the same unread list.
That buys the two things Newsboat
structurally lacks — fetching while your
machine is off, and synchronised reading
across phone and desk. The cost is the
server itself: install, updates, a login,
a database. The series' FreshRSS guide
covers it end to end. Notably, the two
are not enemies: Newsboat can read
*through* a FreshRSS account (a documented
configuration this lab did not run), so
"terminal hands, server memory" is a real
combination.

## Miniflux — the server, minimal

**Miniflux** does the server half with a
plumber's temperament: one Go binary, a
PostgreSQL database, a deliberately plain
web interface, and a thorough API. Where
FreshRSS feels like a product, Miniflux
feels like infrastructure — the series'
Miniflux guide runs it for real. It is
the neighbour to pick when the sync is
the point and the interface is allowed to
be spare, and like FreshRSS it can stand
behind Newsboat as its remote source.

## Liferea — the desktop reader

**Liferea** is the long-standing GNOME
feed reader: a three-pane window, folders
in a tree, reading in place. If your
reading happens at one graphical desk and
your hands prefer a mouse, it asks
nothing of the terminal and gives a
calmer first hour than Newsboat's keys.
What it does not give is the file-level
ownership: subscriptions and state live
in its own stores, in its own formats.

## The hosted readers — Feedly, Inoreader, NewsBlur

The commercial services remove the server
problem entirely: sign up, import OPML,
read anywhere, pay for the tier above
free. NewsBlur, the oldest of them, adds
training filters and a social layer. All
of them hold your subscription list and
reading record on someone else's machine
— precisely the arrangement Newsboat
exists to decline — and all of them are
the right answer for a reader who values
the phone experience over that fact.
Your exit, if it comes, is the same OPML
you went in with (chapter 6), which is
why this guide made a habit of exporting
it.

## The elder: Newsbeuter, and the tiny tools

Newsboat is a fork of **Newsbeuter**, the
reader that proved this design in the
2000s–2010s; Newsbeuter is unmaintained,
and Newsboat is where its users and its
ideas went — several chapters of this
guide (the queue file, Podboat) are
inheritance, maintained. At the other
scale sit one-shot fetch tools and
feed-to-email gateways: right for a
single feed wired into a script or an
inbox, not a reading habit.

The pattern across all of them: decide
where fetching happens (your machine,
your server, their cloud) and where the
reading record lives, and the tool
chooses itself. Newsboat's answers —
your machine, your disk, your files —
are this guide's whole subject.
