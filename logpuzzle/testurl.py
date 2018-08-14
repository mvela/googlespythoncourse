#!/usr/bin/python
import urllib.request
import os
	
def main():
	dest_dir = "imagedir"
	
	#creates directory "imagedir"
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)

	#downloads file into imagedir
	tfile = urllib.request.urlretrieve("https://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg", os.path.join(dest_dir, "testimage.jpg"))

if __name__ == '__main__':
  main()
