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

contexts = configParser.getsubcontexts()
reddit=configParser.getreddit
DataCollector = DataCollector(redditobject=reddit)

def job(sub):
    sorttype = 0
    subname = 0
    timeframe = 0 
    limit = 0 

    sorttype = SortType.get(sub.section.lower())
    sorttime = SortTime.get(sub.time.lower())
    
    subname = sub.subname
    limit = sub.submissions
    DataCollector.collectPostData(sorttype, subname, timeframe, limit)
    #remember we need command here to feed into database

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


for x in contexts:
    schedule.every(x.timing).seconds.do(job, x)

while 1:
    schedule.run_pending()
    time.sleep(1)
