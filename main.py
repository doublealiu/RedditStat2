import praw
import schedule
import threading
import time
import string
from database import Database
from redditCollector import SortTime
from redditCollector import SortType
from redditCollector import DataCollector
from config import Config
from config import SubredditContext

configParser = Config("config.yml")
db = configParser.getDatabase()
Database.createtables(db)

contexts = configParser.getsubcontexts()
reddit=configParser.getReddit()
tracked = configParser.getTrackedPosts(reddit)
DataCollector = DataCollector(redditobject=reddit)

def sub_job(sub, db):
    sorttype = SortType.get(sub.section.lower())
    sorttime = SortTime.get(sub.time.lower())
    subname = sub.subname
    limit = sub.submissions

    postdata = DataCollector.collectPostData(sorttype, subname, sorttime, limit)

    for s in postdata:
        Database.insertpost(db, s, sorttype, sorttime)

def post_job(submission, db):
    Database.inserttracked(db, submission)

def run_threaded(job_func, sub, database):
    job_thread = threading.Thread(target=job_func, args=(sub,database))
    job_thread.start()

for x in contexts:
    schedule.every(x.timing).seconds.do(run_threaded, job_func=sub_job, sub=x, database=db)

for x,y in tracked.items():
    schedule.every(y).seconds.do(run_threaded, job_func=post_job, submission=x, db=db)

while 1:
    schedule.run_pending()
    time.sleep(1)
