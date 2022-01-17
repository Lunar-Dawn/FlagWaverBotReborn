import praw

from flagwaverbot.config import secret, settings

reddit = praw.Reddit(
    client_id=secret['Reddit']['client_id'],
    client_secret=secret['Reddit']['client_secret'],
    username=secret['Reddit']['username'],
    password=secret['Reddit']['password'],
    user_agent=settings['user_agent'],
)
