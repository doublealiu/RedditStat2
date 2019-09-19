import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error

class Database:
    @staticmethod
    def createtables(pool):
        dbcon = pool.get_connection()
        cursor = dbcon.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS subreddit_posts " +
                       "(post_id TEXT NOT NULL, points INT, title TEXT, self_text TEXT, " +
                       "subreddit TEXT, sorttype ENUM('hot', 'new', 'controversial', 'top'), " +
                       "timeframe ENUM('hour', 'day', 'week', 'month', 'year', 'all'), " +
                       "time TIMESTAMP NOT NULL DEFAULT NOW());")
        cursor.execute("CREATE TABLE IF NOT EXISTS tracked_posts (post_id TEXT NOT NULL, points INT, title TEXT, "
                       "self_text TEXT, subreddit TEXT, time TIMESTAMP NOT NULL DEFAULT NOW());")
        dbcon.commit()
        dbcon.close()

    @staticmethod
    def insertpost(pool, submission, sort, time):
        dbcon = pool.get_connection()
        statement = "INSERT INTO subreddit_posts VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())"
        val = (submission.id, submission.score, submission.title, submission.selftext, submission.subreddit.display_name, sort, time)
        cursor = dbcon.cursor()
        cursor.execute(statement, val)
        dbcon.commit()
        dbcon.close()

    @staticmethod
    def inserttracked(pool, submission):
        dbcon = pool.get_connection()
        statement = "INSERT INTO tracked_posts VALUES (%s, %s, %s, %s, %s, NOW())"
        val = (submission.id, submission.score, submission.title, submission.selftext, submission.subreddit.display_name)
        cursor = dbcon.cursor()
        cursor.execute(statement, val)
        dbcon.commit()
        dbcon.close()
