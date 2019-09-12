import mysql.connector
import threading

def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func

@synchronized
def createtables(dbcon):
    dbcon = mysql.connector.Connect(dbcon)
    cursor = dbcon.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS subreddit_posts " +
                   "(post_id TEXT NOT NULL, points INT, title TEXT, self-text TEXT, " +
                   "subreddit TEXT, sorttype ENUM('hot', 'new', 'controversial', 'top'), " +
                   "timeframe ENUM('hour', 'day', 'week', 'month', 'year', 'all'), " +
                   "time TIMESTAMP NOT NULL DEFAULT NOW());")
    cursor.execute("CREATE TABLE IF NOT EXISTS subreddit_posts (post_id TEXT NOT NULL, points INT, title TEXT, "
                   "self-text TEXT, subreddit TEXT, time TIMESTAMP NOT NULL DEFAULT NOW());")
    dbcon.commit()

@synchronized
def insertpost(dbcon, submission, sort, time):
    dbcon = mysql.connector.Connect(dbcon)
    statement = "INSERT INTO subreddit_posts VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())"
    val = (submission.id, submission.score, submission.title, submission.selftext, submission.subreddit.name, sort, time)
    cursor = dbcon.cursor()
    cursor.execute(statement, val)
    dbcon.commit()

@synchronized
def inserttracked(dbcon, submission):
    dbcon = mysql.connector.Connect(dbcon)
    statement = "INSERT INTO subreddit_posts VALUES (%s, %s, %s, %s, %s, NOW())"
    val = (submission.id, submission.score, submission.title, submission.selftext, submission.subreddit.name)
    cursor = dbcon.cursor()
    cursor.execute(statement, val)
    dbcon.commit()