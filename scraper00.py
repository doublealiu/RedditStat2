"""
VERSION: 0.0.1

(c) 2019

FORTNITE: Bad
MINECRAFT: Good
"""

import praw
import time

# initialise read only instance of reddit PRAW interface
reddit = praw.Reddit(client_id='0Gw8-EwymQ-fig',
                     client_secret='Y5kigBf4MmZs-u2m3lh6ZvFjclg',
                     user_agent='my user agent (test)')

# allSubreddits has a list of non-duplicate subreddits in page
allSubreddits = []
# the order of counts corresponds with sub list in allSubreddits
subredditsCount = []

for submission in reddit.subreddit('all').top('all', limit=25):
	#increments through allSubreddits
	i = 0
	found = False
	for existing in allSubreddits:
		if (existing == submission.subreddit):
			# increments count for the found subreddit
			subredditsCount[i] = subredditsCount[i] + 1
			found = True
			break	
		i = i + 1
	# appends new subreddit if not found in array
	if (found == False):
		allSubreddits.append(submission.subreddit)
		subredditsCount.append(1)

# for testing - prints out result
for x in allSubreddits:
	print(x)
for y in subredditsCount:
	print(y)