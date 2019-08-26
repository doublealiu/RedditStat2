"""
VERSION: 0.0.2

(c) 2019

FORTNITE: Bad
MINECRAFT: Good
"""

import praw
import time

reddit = praw.Reddit(client_id='0Gw8-EwymQ-fig',
                     client_secret='Y5kigBf4MmZs-u2m3lh6ZvFjclg',
                     user_agent='my user agent (test)')

def listAllSubreddits (timeframe, limit):
	"""
	listAllSubreddits:
	Parameters
	----------

	timeframe: str
		the specified timeframe to view posts (24h, all time, etc)
	limit : int
		the amount of posts desired to grab

	Return
	------
	Returns limit submissions from the specified timeframe : dictionary
		String contains name of subreddit and int contains number of times appeared

	"""
	allSubreddits = {} 
	for submission in reddit.subreddit('all').top(timeframe, limit=limit):
		existing = allSubreddits.get(submission.subreddit, 0)
		if (existing == 0):
			allSubreddits[submission.subreddit] = 1
		else:
			allSubreddits[submission.subreddit] = allSubreddits[submission.subreddit] + 1

	return allSubreddits

def trackUpvotes (postID):
	"""
	trackUpvotes:
	Parameters
	----------

	postID: str
		the post ID in the URL of desired reddit post (ex: 5or86n)
	
	Return
	______
	Returns score (votes) of reddit submission : int
	"""
	submission = reddit.submission(id=postID)
	return submission.score

def findGap(subreddit, pairs, gap):
	"""
	findGap:
	Parameters
	__________
	
	pairs: int
		the amount of analysis on post frequency to be done
		the amount of time gaps between two posts to be calculated

	gap : int 
		the amount of posts between which an analysis is to be done
		(setting gap to 1 will produce highly innacurate data as
		two posts' time differences are mostly within the same second)

	subreddit : str
		the subreddit where you want the analysis to be performed

	Return
	______
	returns average time between new posts on r/all : float
	"""
	times = []
	i = 0
	for submission in reddit.subreddit('all').new(limit=((pairs + 1) * gap)):
		if((i % gap) == 0):
			times.append(submission.created_utc)
		i = i + 1

	differences = 0.0
	i = 0
	for x in times:
		if (i == (len(times) - 1)):
			break
		differences = differences + (times[i] - times[i+1])
		i = i + 1
	return(differences / float(pairs))


# TODO determine whether findGap() is actually accurate
print(findGap('all', 20, 20))

"""
TESTING GROUNDS
_______________
print(trackUpvotes('cuds18'))
time.sleep(20)
print(trackUpvotes('cuds18'))

for x,y in listAllSubreddits('all', 100).items():
	print(x,y)
"""
