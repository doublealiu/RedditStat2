import mysql.connector

def createtables(dbcon):
    dbcon = mysql.connector.Connect(dbcon)
    cursor = dbcon.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS webscraper_database")
    cursor.execute("CREATE TABLE IF NOT EXISTS subreddit_posts (post_id TEXT, points INT, title TEXT, self-text TEXT, " +
                   "subreddit TEXT, sorttype ENUM('hot', 'new', 'controversial', 'top'), " +
                   "timeframe ENUM('hour', 'day', 'week', 'month', 'year', 'all'), time TIMESTAMP)")
    cursor.execute("CREATE TABLE IF NOT EXISTS subreddit_posts (post_id TEXT, points INT, title TEXT, "
                   "self-text TEXT, time TIMESTAMP)")
    dbcon.commit()

def insertsubreddit(post_id, subreddit):
