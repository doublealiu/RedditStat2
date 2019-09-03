"""
VERSION: 0.0.2

(c) 2019

FORTNITE: Bad
MINECRAFT: Good
"""
import praw
import time  # remove later
import string
# import config
import emoji
from enum import Enum


class SortType(Enum):
    """
	Please note that timeframe is only used for controversial and top sorting methods
	"""
<<<<<<< HEAD

    def HOT(subreddit, timeframe, limit):
        return reddit.subredit(subreddit).hot(limit=limit)

    def NEW(subreddit, timeframe, limit):
        return reddit.subreddit(subreddit).new(limit=limit)

    def CONTROVERSIAL(subreddit, timeframe, limit):
        return reddit.subreddit(subreddit).controversial(timeframe, limit=limit)

    def TOP(subreddit, timeframe, limit):
        return reddit.subreddit(subreddit).top(timeframe, limit=limit)


# config = config.Config()
=======
	def HOT(subreddit, timeframe, limit):
		return reddit.subredit(subreddit).hot(limit=limit)
	def NEW(subreddit, timeframe, limit):
		return reddit.subreddit(subreddit).new(limit=limit)
	def CONTROVERSIAL(subreddit, timeframe, limit):
		return reddit.subreddit(subreddit).controversial(timeframe, limit=limit)
	def TOP(subreddit, timeframe, limit):
		return reddit.subreddit(subreddit).top(timeframe, limit=limit)

#config = config.Config()
>>>>>>> 131e4c93f3f03027e1507809fc1f38236ac66469
reddit = praw.Reddit(client_id='0Gw8-EwymQ-fig',
                     client_secret='Y5kigBf4MmZs-u2m3lh6ZvFjclg',
                     user_agent='my user agent (test)')


def listAllSubreddits(type, timeframe, limit):
    """
	listAllSubreddits:
	Parameters
	----------

	type: SortType
		the specified type of reddit sort to list all subreddits
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
    # for submission in reddit.subreddit('all').top(timeframe, limit=limit):
    for submission in type('all', timeframe, limit):
        existing = allSubreddits.get(submission.subreddit, 0)
        if (existing == 0):
            allSubreddits[submission.subreddit] = 1
        else:
            allSubreddits[submission.subreddit] = allSubreddits[submission.subreddit] + 1

    return allSubreddits


def trackUpvotes(postID):
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


def findGap(sub, pairs, gap):
    """
	findGap:
	Parameters
	__________
	
	sub : str
		the subreddit where you want the analysis to be performed
	pairs: int
		the amount of analysis on post frequency to be done
		the amount of time gaps between two posts to be calculated
	gap : int 
		the amount of posts between which an analysis is to be done
		(setting gap to 1 will produce highly innacurate data as
		two posts' time differences are mostly within the same second)


	Return
	______
	returns average time between new posts on r/all : float
	"""
    times = []
    i = 0
    for submission in SortType.NEW(sub, 'all', limit=((pairs + 1) * gap)):
        if ((i % gap) == 0):
            times.append(submission.created_utc)
        i = i + 1

    differences = 0.0
    i = 0
    for x in times:
        if (i == (len(times) - 1)):
            break
        differences = differences + (times[i] - times[i + 1])
        i = i + 1
    return (differences / float(pairs))


def frequentWords(type, sub, timeframe, limit):
    """
	frequentWords:
	Parameters
	__________

	type: SortType
		the specified type of reddit sort to list all subreddits
	sub: str
		the subreddit where you want to analze the most frequent words 
	timeframe: str
		the timeframe of posts you want to search through
	limit: int
		the number of posts you want analyzed

	Return
	______
	returns dictionary with string of word (all lowercase) and frequency : string, int

	"""
    allWords = {}
    line = []
    out = ""
    for submission in type(sub, timeframe, limit):
        line = submission.title.split()
        for x in line:
            out = x.translate(str.maketrans('', '', string.punctuation)).lower()
            if (out.isdigit()):
                continue

            existing = allWords.get(out, 0)
            if (existing == 0):
                allWords[out] = 1
            else:
                allWords[out] = allWords[out] + 1

    return allWords


def frequentEmoji(type, sub, timeframe, limit):
    """
	frequentEmoji:
	Parameters
	__________

	type: SortType
		the specified type of reddit sort to list all subreddits
	sub: str
		the subreddit where you want to analze the most frequent emoji 
	timeframe: str
		the timeframe of posts you want to search through
	limit: int
		the number of posts you want analyzed

	Return
	______
	returns dictionary with emoji and frequency: string, int
	"""
    allEmoji = {}
    emojiLine = []
    for submission in type(sub, timeframe, limit):
        for emoticon in (submission.title + submission.selftext):
            if (emoticon in emoji.UNICODE_EMOJI):
                existing = allEmoji.get(emoticon, 0)
                if (existing == 0):
                    allEmoji[emoticon] = 1
                else:
                    allEmoji[emoticon] = allEmoji[emoticon] + 1
    return allEmoji


for x, y in frequentWords(SortType.TOP, 'amitheasshole', 'all', 20).items():
    print(x, y)
"""
TESTING GROUNDS
_______________
for x,y in listAllSubreddits(SortType.TOP, 'all', 100).items():
	print(x,y)
print(trackUpvotes('cuds18'))
time.sleep(20)
print(trackUpvotes('cuds18'))

for x,y in listAllSubreddits('all', 100).items():
	print(x,y)

# TODO determine whether findGap() is actually accurate
print(findGap('all', 20, 20))

for x,y in frequentWords(SortType.HOT, 'all', 'all', 10).items():
	print(x,y)

for x,y in frequentWords('all', 500).items():
	print(x,y)

for x,y in frequentEmoji('emojipasta', 10).items():
	print(x,y)
"""
