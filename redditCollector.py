import praw
import string

class SortTime():
    @staticmethod
    def hour():
        return "hour"
    @staticmethod
    def day():
        return "day"
    @staticmethod
    def week():
        return "week"
    @staticmethod
    def month():
        return "month"
    @staticmethod
    def year():
        return "year"
    @staticmethod
    def all():
        return "all"

class SortType():
    """
        Please note that timeframe is only used for controversial and top sorting methods
    """
    @staticmethod
    def hot(reddit, subreddit, timeframe, limit):
        return reddit.subreddit(subreddit).hot(limit=limit)
    @staticmethod
    def new(reddit, subreddit, timeframe, limit):
        return reddit.subreddit(subreddit).new(limit=limit)
    @staticmethod
    def controversial(reddit, subreddit, timeframe, limit):
        return reddit.subreddit(subreddit).controversial(timeframe, limit=limit)
    @staticmethod
    def top(reddit, subreddit, timeframe, limit):
        return reddit.subreddit(subreddit).top(timeframe, limit=limit)

class DataCollector:
    reddit = 0
    def __init__ (self, redditobject):
        self.reddit = redditobject

    def collectPostData(self, sorttype, sub, timeframe, limit):
        postArray = []
        for submission in sorttype(self.reddit, sub, timeframe, limit):
            postArray.append(submission)
        return postArray

    def collectSinglePost(self, postId):
        submission = self.reddit.submission(id=postId)
        return submission

reddit = praw.Reddit(client_id='0Gw8-EwymQ-fig',
                     client_secret='Y5kigBf4MmZs-u2m3lh6ZvFjclg',
                     user_agent='my user agent (test)')
yeettest = DataCollector(reddit)
yeettest.collectPostData(sorttype=SortType.hot, sub='all', timeframe=SortTime.week, limit=25)
