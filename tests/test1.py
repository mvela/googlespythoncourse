#!usr/bin/python
"""takes a string and returns the string in a random order"""
import random


def strtest(aString):
	"""this function takes the string and returns the string in a random order"""	
	
	newstring = random.sample(aString, len(aString))
	newstring = "".join(newstring)
	return(newstring)
