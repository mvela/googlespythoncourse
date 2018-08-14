#!/usr/bin/python 
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Usage: python logpuzzle.py --todir (directory destinatino) (file)

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def helper_sort(url):
	
	return url[-9:-1]

def read_urls(filename):
	"""Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
	# +++your code here+++
 	
	#retrieve host name
	host = filename[filename.index('_') + 1:]
	print(host)

	#open the file and read it into a string
	f = open(filename, 'r')
	rString = f.read()
	f.close()
	
	#finds all " /(NoSpaceCharacters) " and puts it in a list that is then sorted
	match = re.findall("\s\S+puzzle\S+-\S+-\S+.jpg\s", rString)

	if not match:
		match = re.findall("\s\S+.jpg\s", rString)
		match = sorted(match)
	else:
		match = sorted(match, key=helper_sort)

	#initialize lists
	#added_urls is added to verify that there are not duplicates
	allUrls = []
	added_urls = []
	
	#for all urls in match that have not been added already
	#add them to a list and append "code.google.com" with each url
	for url in match:
		if url not in added_urls:
			allUrls.append("https://" + host + url.strip())
		added_urls.append(url)
	
	return allUrls

def download_images(img_urls, dest_dir):
	"""Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
	"""
	# +++your code here+++
  
	#create the directory for the downloaded images
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)
	f = open(os.path.join(dest_dir,"index.html"), 'w')
	f.write("<verbatim>\n<html>\n<body>\n")
	
	#download all images from each url to the destinated directory
	i = 0
	for img in img_urls:
		print("Downloading %s" % img, flush=True)	
		urllib.request.urlretrieve(img, os.path.join(dest_dir, "img%d.jpg"  % i ))
		f.write("<img src=\"img%d.jpg\">" %i)
		i += 1
	
	f.write("</body>\n</html>")
	f.close()

def main():
	args = sys.argv[1:]
	if not args:
		print ('usage: [--todir dir] logfile ')
		sys.exit(1)

	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]

	img_urls = read_urls(args[0])

	if todir:
		download_images(img_urls, todir)
	else:
		print ('\n'.join(img_urls))

if __name__ == '__main__':
	main()
