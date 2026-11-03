#!/bin/sh
# A stand-in "browser" for the lab: instead of opening a page, it
# records the URL Newsboat handed it and prints the page's title
# line, proving the handoff happened and with what address.
# The lab also runs one session with a real text browser (w3m);
# this script exists so the handoff itself can be checked in a
# transcript without a browser's full screen getting in the way.
log="${NB_BROWSER_LOG:-$HOME/browser-log.txt}"
echo "$1" >> "$log"
echo "The browser was handed this URL: $1"
curl -s "$1" | grep -o '<title>[^<]*</title>' | head -1
echo "(Press Enter to return to Newsboat.)"
read -r _dummy
