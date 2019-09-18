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

def post_job(tracked, db):
    Database.inserttracked(db, DataCollector.collectSinglePost(tracked))

def run_threaded(job_func, sub, database):
    job_thread = threading.Thread(target=job_func, args=(sub,database))
    job_thread.start()

for context in contexts:
    schedule.every(context.timing).seconds.do(run_threaded, job_func=sub_job, sub=context, database=db)

for id, timing in tracked.items():
    schedule.every(timing).seconds.do(run_threaded, job_func=post_job, submission=id, db=db)

while 1:
    schedule.run_pending()
    time.sleep(1)
