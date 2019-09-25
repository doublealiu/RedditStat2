import yaml
import mysql.connector
import praw.reddit
from mysql.connector import pooling

#   Represents the state of config.yml at the time that it is called,
#   nonmutable and will only return data about the config at the time it is called

class Config(object):
    def __init__(self, filename):
        file = open(filename, 'r')
        self.data = yaml.safe_load(file)
        file.close()

    def getDatabase(self):
        dbData = self.data.get("database")
        return mysql.connector.pooling.MySQLConnectionPool(pool_name="schedulepool", pool_size=10, pool_reset_session=True,
                                                           host=dbData.get("host"), database=dbData.get("database-name"),
                                                           user=dbData.get("username"), password=dbData.get("password"))

    def getTrackedPosts(self, reddit):
        idlist = self.data.get("track-posts")
        submissions = dict()
        if idlist is None:
            return submissions
        for postid in idlist:
            submission = reddit.submission(id=postid)
            if submission is not None:
                submissions[postid] = idlist[postid]
        return submissions

    def getReddit(self):
        redditData = self.data.get("reddit")
        return praw.Reddit(client_id=redditData.get("client-id"), client_secret=redditData.get("client-secret"),
                           user_agent=redditData.get("user-agent"))

    def getsubcontexts(self):
        subsdata = self.data.get("subreddits")
        subs = list()
        for sub in subsdata.keys():
            datacollect = subsdata.get(sub)
            singlesub = SubredditContext(sub, datacollect.get("submissions"), datacollect.get("timing"),
                                         datacollect.get("sort-by-section"), datacollect.get("sort-by-time"))
            subs.append(singlesub)
        return subs

class SubredditContext:
    def __init__(self, subname, submissions, timing, section, time):
        self.subname = subname
        self.submissions = submissions
        self.timing = timing
        self.section = section
        self.time = time
