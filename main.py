import praw
import schedule
import threading
import time
import string
import database
from redditCollector import SortTime
from redditCollector import SortType
from redditCollector import DataCollector
from config import Config
from config import SubredditContext

configParser = Config("config.yml")
db = configParser.getDatabase()
database.createtables(db)

contexts = configParser.getsubcontexts()
reddit=configParser.getreddit
DataCollector = DataCollector(redditobject=reddit)

def sub_job(sub, db):
    sorttype = SortType.get(sub.section.lower())
    sorttime = SortTime.get(sub.time.lower())
    subname = sub.subname
    limit = sub.submissions

    postdata = DataCollector.collectPostData(sorttype, subname, sorttime, limit)

    for s in postdata:
        database.insertpost(db, s, sorttype, sorttime)

def run_threaded(job_func, sub, database):
    job_thread = threading.Thread(target=job_func, args=(sub,database))
    job_thread.start()

for x in contexts:
    schedule.every(x.timing).seconds.do(run_threaded, job_func=sub_job, sub=x, database=db)

while 1:
    schedule.run_pending()
    time.sleep(1)
