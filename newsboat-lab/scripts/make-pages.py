#!/usr/bin/env python3
"""Generate a simple HTML page for every article in the fixture feeds.

The two showcase pages (tomatoes, knife) are hand-written and kept;
this fills in the rest so every link in the fixture feeds resolves on
the lab's web server. Each generated page carries the article's title
and the same text the feed itself carries -- no new claims.

Usage: make-pages.py FIXTURES_DIR WWW_DIR
"""
import os
import sys
import urllib.parse
import xml.etree.ElementTree as ET

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>{title} — {feed}</title></head>
<body>
<h1>{title}</h1>
<p><em>{feed} — a fixture page invented for this guide's lab.</em></p>
<p>{body}</p>
</body>
</html>
"""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def emit(feed_title, title, link, body, www):
    path = urllib.parse.urlparse(link).path.lstrip("/")
    dest = os.path.join(www, path)
    if os.path.exists(dest):
        print("kept (hand-written):", path)
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        fh.write(TEMPLATE.format(title=esc(title), feed=esc(feed_title),
                                 body=esc(body)))
    print("wrote:", path)


def main():
    fixtures, www = sys.argv[1], sys.argv[2]
    rss = ET.parse(os.path.join(fixtures, "feeds", "garden-notes.xml"))
    chan = rss.getroot().find("channel")
    feed_title = chan.findtext("title")
    for item in chan.findall("item"):
        emit(feed_title, item.findtext("title"), item.findtext("link"),
             item.findtext("description"), www)
    pod = ET.parse(os.path.join(fixtures, "feeds", "workshop-podcast.xml"))
    chan = pod.getroot().find("channel")
    feed_title = chan.findtext("title")
    for item in chan.findall("item"):
        emit(feed_title, item.findtext("title"), item.findtext("link"),
             item.findtext("description"), www)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    atom = ET.parse(os.path.join(fixtures, "feeds", "kitchen-journal.xml"))
    root = atom.getroot()
    feed_title = root.findtext("a:title", namespaces=ns)
    for entry in root.findall("a:entry", ns):
        emit(feed_title, entry.findtext("a:title", namespaces=ns),
             entry.find("a:link", ns).get("href"),
             entry.findtext("a:summary", namespaces=ns), www)


if __name__ == "__main__":
    main()
