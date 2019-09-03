import praw
from scraper import ScraperMachine
from scraper import SortType
import schedule
import threading
import time


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def hi():
    print("hi works")


reddit = praw.Reddit(client_id='0Gw8-EwymQ-fig',
                     client_secret='Y5kigBf4MmZs-u2m3lh6ZvFjclg',
                     user_agent='my user agent (test)')

scraper1 = ScraperMachine(redditobject=reddit)
for x,y in scraper1.listAllSubreddits(type=SortType.top, timeframe='all', limit=25).items():
	print(x,y)
