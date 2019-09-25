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
    if (subname == "all"):
        for s in postdata:
            Database.insertallpost(db, s, SortType.getName(sorttype), SortTime.getName(sorttime))
    else:
        for s in postdata:
            Database.insertpost(db, s, SortType.getName(sorttype), SortTime.getName(sorttime))

def post_job(tracked, db):
    Database.inserttracked(db, DataCollector.collectSinglePost(tracked))

def run_threaded(func, sub, db):
    job_thread = threading.Thread(target=func, args=(sub, db))
    job_thread.start()

for context in contexts:
    schedule.every(context.timing).seconds.do(job_func=run_threaded, func=sub_job, sub=context, db=db)

for id, timing in tracked.items():
    schedule.every(timing).seconds.do(job_func=run_threaded, func=post_job, sub=id, db=db)

while 1:
    schedule.run_pending()
    time.sleep(1)
