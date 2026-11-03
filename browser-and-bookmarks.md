# The Browser and Bookmarks

Outcome: an article can leave the terminal
for a real web page and come back, and
"bookmark" can mean whatever your own
script says it means.

## Out to the browser

A feed carries a summary, or sometimes a
stub; the article's home is its web page.
In the article view, `o` (open in browser)
hands the link to whatever the `browser`
setting names. Newsboat is deliberately
agnostic about what that is — a graphical
browser, a text browser, or a script —
which the lab proved with the strictest
possible witness, a script that only
writes down what it was handed:

```text
browser "/path/to/show-url.sh %u"
```

The `%u` is where the article's address
goes. With that config, opening the seedling
article produced, on screen and in the
script's log:

```text
The browser was handed this URL: http://127.0.0.1:18089/garden/seedlings-lean.html
```

and the script fetched the page's title
to show it had been given a working
address. Swap the script for a browser and
nothing else changes. With a real text
browser —

```text
browser "w3m %u"
```

— the same `o` opened the article's page
inside w3m, rendered as a web page
(heading, paragraphs, the lab's fixture
note and all), and `q` in w3m, confirmed
with `y`, handed the terminal back to
Newsboat with the article still open. A
graphical browser named the same way
behaves the same less politely: Newsboat
waits for it to exit, so on a desktop you
would typically append `&` in the command
or use your system's opener — the
mechanism is identical, only the string
differs.

One habit this creates: because the
handoff is just a command, the "browser"
can also be `curl`-into-a-file, a
read-later service's add-script, or a
logger — the same trick the next section
uses on purpose.

## Bookmarks: a contract with a script

Newsboat has no bookmark store of its
own. Instead it has `bookmark-cmd`: a
program of yours that Newsboat calls with
four arguments — the article's address,
its title, its description, and its feed
title. Whatever should happen to a
bookmark is that program's business.

In any article, `Ctrl-B` opens a short
round of prompts along the bottom of the
screen, pre-filled with those values:

```text
URL: http://127.0.0.1:18089/garden/soil-test-jar.html
```

Accept or edit each with Enter (the
description starts empty; the feed's own
text is not forced into it), and the last
Enter runs your command. The lab's
command was a nine-line shell script that
appends the four values to a text file —
and the file afterwards is the whole
result:

```text
URL:         http://127.0.0.1:18089/garden/soil-test-jar.html
Title:       A five-minute soil test with a jam jar
Description:
Feed:        The Example Garden Notes
```

That script is in `newsboat-lab/scripts/`
and is deliberately trivial. Real ones
append to a notes file with a date,
insert into a links database, post to a
read-later service, or file the address
under the day's journal heading. The
point of the design is the one this whole
tool keeps making: the decision lives in
a file you own, in a language you know,
and Newsboat's part is only to show up
with the four facts at the moment you
pressed the keys.

Check: point `bookmark-cmd` at the lab
script (or `echo` into a file of your
own), bookmark one article, and read the
result outside Newsboat entirely.
