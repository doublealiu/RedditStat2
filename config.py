import yaml
import mysql.connector
import praw.reddit

#   Represents the state of config.yml at the time that it is called,
#   nonmutable and will only return data about the config at the time it is called

class Config(object):
    def __init__(self, filename):
        file = open(filename, 'r')
        self.data = yaml.safe_load(file)
        file.close()

    def getDatabase(self):
        dbData = self.data.get("database")
        return mysql.connector.connect(host = dbData.get("host"), database = dbData.get("database-name"), user = dbData.get("username"), password = dbData.get("password"))

    def getTrackedPosts(self, reddit):
        reddit = reddit(reddit)
        idList = self.data.get("tracked-posts")
        submissions = list()
        for id in idList:
            submission = reddit.submission(id=id)
            if submission is not None:
                submissions.append(submission)
        return submissions

    def getReddit(self):
        redditData = self.data.get("reddit")
        return praw.Reddit(client_id = redditData.get("client-id"), client_secret = redditData.get("client-secret"), user_agent = redditData.get("user-agent"))

    def getsubcontexts(self):
        subsdata = self.data.get("subreddits")
        subs = list()
        for sub in subsdata.keys:
            datacollect = sub.get("data")
            singlesub = SubredditContext(sub.get("submissions"), sub.get("timing"), sub.get("sort-by-section"), sub.get("sort-by-time"), datacollect.get("title"), datacollect.get("points"), datacollect.get("self-text"))
            subs.append(singlesub)

class SubredditContext:
    def __init__(self, subname, submissions, timing, section, time, title, points, selftext):
        self.subname = subname
        self.submissions = submissions
        self.timing = timing
        self.section = section
        self.time = time
        self.title = title
        self.points = points
        self.selftext = selftext