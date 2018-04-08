#! python3
# hashtagcount.py - Quickly check how many hashtags you have before posting to Instagram. Supply as command line argument in "". 

import sys

#Check to make sure hashtags are supplied as command line argument.
if len(sys.argv) < 2:
	print("Please enter some hashtags to count. Use a command line argument.")
	sys.exit()

#Import hashtags into dictionary
dictionary = str(sys.argv[1:])

#Print how many hashtags you have.
print("You have {} hashtags.".format(dictionary.count("#")))
