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

#database.createtables()
configParser = Config("config.yml")
contexts = []
contexts = configParser.getsubcontexts()

reddit = praw.Reddit(client_id='0Gw8-EwymQ-fig',
                     client_secret='Y5kigBf4MmZs-u2m3lh6ZvFjclg',
                     user_agent='my user agent (test)')

DataCollector = DataCollector(reddit)

def job(sub):
    sorttype = 0
    subname = 0
    timeframe = 0 
    limit = 0 

    if(sub.section.lower() == "hot"):
        sorttype = SortType.hot
    elif(sub.section.lower() == "top"):
        sorttype = SortType.top
    elif(sub.section.lower() == "controversial"):
        sorttype = SortType.controversial
    elif(sub.section.lower() == "new"):
        sorttype = SortType.new
    else:
        sorttype = SortType.top

    if(sub.time.lower() == "hour" || sub.time.lower() == "h"):
        timeframe = SourtTime.hour
    elif(sub.time.lower() == "today" || sub.time.lower() == "day" || sub.time.lower() == "24h"):
        timeframe = SortTime.day
    elif(sub.time.lower() == "week"):
        timeframe = SortTime.week
    elif(sub.time.lower() == "year" || sub.time.lower() == "y"):
        timeframe = SortTime.year
    elif(sub.time.lower() == "all"):
        timeframe = SortTime.all
    else:
        timeframe = SortTime.day
    
    subname = sub.subname
    limit = sub.submissions
    DataCollector.collectPostData(sorttype, subname, timeframe, limit)
    
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


for x in contexts:
    schedule.every(x.timing).seconds.do(job, sub=x)

while 1:
    schedule.run_pending()
    time.sleep(1)
