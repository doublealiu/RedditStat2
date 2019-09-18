# RedditStat
A python script that controls a reddit bot. The bot will read data (specified in config) and write that data to a database. Features include:
 * tracking upvotes over time
 * tracking frequently used words or emoji
 * tracking which subreddits reach the frontpage (r/all)
 * tracking frequency of activity on specified subreddits

## Dependencies
RedditStat uses [Python 3.7.4](https://www.python.org/downloads/). Make sure to have PRAW, PyYAML, schedule, and mysql-connector installed. 
```
pip3 install praw --upgrade
pip3 install pyyaml --upgrade
pip3 install schedule --upgrade
pip3 install mysql-connector --upgrade
```
If ```pip3``` does not work, use ```pip```. 

## Reddit Instance
To use RedditStat, you will need a reddit account with a custom "developed application" added. 
1. Create an account on reddit, or sign in. The username is not important as RedditStat is read-only.
2. In https://old.reddit.com/prefs/apps/, click *create another app...* 
3. Select the *script* option and put a basic description and name. Click *create app.*
4. Your ```client_id``` is under the heading "personal use script" while ```client_secret``` is next to "secret."

## Configuration
Most configuration features are implemented in the example config.yml file below:
```
database:
# Database section is required
# Database is compatible with most modern implementations of mysql (8.0 / phpmyadmin)
  host: test.com #can be an IP address or URL
  database-name: test
  username: root
  password: password

subreddits:
  linuxmasterrace: #subreddit name (string after /r/)
    submissions: 50 #select 50 submissions
    timing: 60 #get data every 60 seconds
    sort-by-section: hot #hot, top, controversial; defaults to hot if not any of those
    sort-by-time: today #only works with controversial and top; hour, day, week, month, year, all

track-posts:
  # obtain a post url: ex. https://www.reddit.com/r/learnprogramming/comments/61oly8/new_read_me_first/
  61oly8: 20 # post ID is always the 6 character string after "/comments/." Will refresh every 20 seconds

reddit:
#Reddit section is required (refer to subheading Reddit Instance)
  client-id: dsds
  client-secret: dsa
  user-agent: dsafvfd # not dependent for program execution
```

