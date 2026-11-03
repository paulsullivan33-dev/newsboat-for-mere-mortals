#!/bin/sh
# A bookmark-cmd for the lab: Newsboat calls it with four arguments --
# the URL, the title, the description and the feed title -- and the
# lab's version simply appends them to a plain-text bookmarks file,
# which is all a real bookmark script has to do with them.
# The file lives next to the lab HOME; NB_BOOKMARKS overrides it.
out="${NB_BOOKMARKS:-$HOME/bookmarks.txt}"
{
    echo "URL:         $1"
    echo "Title:       $2"
    echo "Description: $3"
    echo "Feed:        $4"
    echo "---"
} >> "$out"
