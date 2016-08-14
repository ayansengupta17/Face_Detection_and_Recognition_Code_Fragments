#!/bin/bash
#This script downloads the images from the given google url.
search_string=$1
google_path="https://www.google.co.in/search?q="
query_path="&tbm=isch"
im_path=$google_path$search_string$query_path
mkdir $search_string
echo "Downloading" $search_string "images"
wget -U "Mozilla" $im_path -O filename
grep -E -o "<a href=\"\/url\?q=https\:/\/*.*\">" filename > dump.txt
python generate_urls.py
while read line
do
wget $line -P ~/Documents/Research/codes/Mined_pics/$search_string
done < links.txt

