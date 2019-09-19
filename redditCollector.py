import praw
import string

class SortTime():
    @staticmethod
    def get(name):
        name = name.lower()
        timeframe = 0
        if(name == "hour" or name == "h"):
            timeframe = SortTime.hour
        elif(name == "today" or name == "day" or name == "24h"):
            timeframe = SortTime.day
        elif(name == "week"):
            timeframe = SortTime.week
        elif(name == "year" or name == "y"):
            timeframe = SortTime.year
        elif(name == "all"):
            timeframe = SortTime.all
        else:
            timeframe = SortTime.hour
        return timeframe

    @staticmethod
    def getName(method):
        if method==SortTime.hour:
            return "hour"
        if method==SortTime.day:
            return "day"
        if method==SortTime.week:
            return "week"
        if method==SortTime.year:
            return "year"
        if method==SortTime.all:
            return "all"
        return 0

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
    def get(name):
        name = name.lower()
        sorttype = 0
        if(name == "hot"):
            sorttype = SortType.hot
        elif(name == "top"):
            sorttype = SortType.top
        elif(name == "controversial"):
            sorttype = SortType.controversial
        elif(name == "new"):
            sorttype = SortType.new
        else:
            sorttype = SortType.hot
        return sorttype

    @staticmethod
    def getName(method):
        if method==SortType.hot:
            return "hot"
        if method==SortType.new:
            return "new"
        if method==SortType.controversial:
            return "controversial"
        if method==SortType.top:
            return "top"
        return 0

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
        return sorttype(self.reddit, sub, timeframe, limit)

    def collectSinglePost(self, postId):
        submission = self.reddit.submission(id=postId)
        return submission
