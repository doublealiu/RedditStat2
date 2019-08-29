# RedditStat
A python script that controls a reddit bot. The bot will read data (specified in config) and write that data to a database. Features include:
 * tracking upvotes over time
 * tracking frequently used words or emoji
 * tracking which subreddits reach the frontpage (r/all)
 * tracking frequency of activity on specified subreddits

## Dependencies
RedditStat uses [Python 3.7.4](https://www.python.org/downloads/). Make sure to have PRAW, PyYAML, and emoji installed. 
```
pip3 install praw --upgrade
pip3 install pyyaml --upgrade
pip3 install emoji --upgrade
```
If ```pip3``` does not work, use ```pip```. 

## Reddit Instance
To use RedditStat, you will need a reddit account with a custom "developed application" added. 
1. Create an account on reddit. The username is not important as RedditStat is read-only.
2. In https://old.reddit.com/prefs/apps/, click *create another app...* 
3. Select the *script* option and put a basic description and name. Click *create app.*
4. Your ```client_id``` is under the heading "personal use script" while ```client_secret``` is next to "secret."
