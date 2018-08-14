#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
	
import sys
import re
import os
import shutil

"""Copy Special exercise
	 Usage: python copyspecial.py --todir (directory ('.', './dir', etc)) sourcefile
"""

# +++your code here+++
# Write functions and modify main() to call them

def getPaths(filedir):
	"""returns the absolute path for a directory"""
	abspath = os.path.abspath(filedir)
	print(abspath)
	return

def todir(filelist, filedir):
	"""copies files to specified directory"""
	print("todir")
	getPaths(filedir)
	shutil.copy(filelist, filedir)
	return
	

def main():
	# This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
	args = sys.argv[1:]
	if not args:
		print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
		sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
	tod = ''
	toz = ''
	
	if args[0] == '--todir':
		tod = args[1]
		del args[0:2]

	elif args[0] == '--tozip':
		toz = args[1]
		del args[0:2]

	elif len(args) == 0:
		print ("error: must specify one or more dirs")
		sys.exit(1)

  # +++your code here+++
  # Call your functions
	
	#paths = []
  #print(paths.extend(get_special_paths(dirname)))

	if tod is not None:
		todir(args[0], tod)	
	
	elif toz is not None:
		tozip(toz)	

if __name__ == "__main__":
	main()
