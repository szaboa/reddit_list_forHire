#!/bin/sh
from datetime import datetime
import requests
import time
import sys
import getopt


LIMIT = '20'
DAY = '1'
KEYWORD = 'android'
MODE = '0'

def main(argv):
	try:
		opts, args = getopt.getopt(argv,'l:s:k:m:h', ['limit=', 'day=','keyword=', 'mode=', 'help'])
	except getopt.GetoptError:
		showHelp()
		sys.exit(2)

	if not opts and args:
		showHelp()
		sys.exit(2)


	for opt, arg in opts:
		if opt in ('-l', '--limit'):
			global LIMIT
			LIMIT = arg
		elif opt in ('-d', '--day'):
			global day
			DAY = arg
		elif opt in ('-k', '--keyword'):
			global KEYWORD
			KEYWORD = arg
		elif opt in ('-m', '--mode'):
			global MODE
			MODE = arg
		elif opt in ('-h', '--help'):
			showHelp()
			sys.exit(2)
		else:
			showHelp()
			sys.exit(2)

	if not isValidArgs():
		showHelp()
		sys.exit(2) 

def isValidArgs():
	return LIMIT.isdigit() and DAY.isdigit()  and MODE.isdigit()
		
def showHelp():
	print 'Listing /forHire subreddit posts with given arguments \n'
	print 'reddit_hiring [-l | --limit] [-d | --day] [-k | --keyword] [-m | --mode] [-h | --help]'
	print '\t l \t Number of post limit (default value 20)'
	print '\t d \t Posts from d days ago (default value 1)'
	print '\t k \t Search keyword for title / description'
	print '\t m \t 0 - For hire | 1 - Hiring | 2 - Both (default value 0)' 
	print '\t h \t Help'

if __name__ == "__main__":
	main(sys.argv[1:])

