#!/usr/bin/python

import random
import test1

def main():
		
		string1 = "this is a string"
		string2 = test1.strtest(string1)
		
		print(string2)
		help(test1)
		
		print("strtest function in test1 module: ")
		print(test1.strtest.__doc__)

		print("\n" + "help on random: ")
		help(random)

if __name__ == "__main__":
	main()
