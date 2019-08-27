# RedditStat
A python script that controls a reddit bot. The bot will read data (specified in config) and write that data to a database. Features include:
 * tracking upvotes over time
 * tracking frequently used words or emoji
 * tracking which subreddits reach the frontpage (r/all)
 * tracking frequency of activity on specified subreddits

# Dependencies
RedditStat uses Python 3.7.4. (https://www.python.org/downloads/) Make sure to have PRAW, PyYAML, and emoji installed. 
```
pip3 install praw --upgrade
pip3 install pyyaml --upgrade
pip3 install emoji --upgrade
```
If pip3 does not work use ```pip```. 
