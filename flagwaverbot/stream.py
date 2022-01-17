from typing import List, Union

import praw.models

from flagwaverbot.bot import reddit
from flagwaverbot.config import settings


subreddits = reddit.subreddit('+'.join(settings['subreddits']))


def comments_submissions_and_mentions(**kwargs) -> List[Union[praw.models.Comment, praw.models.Submission]]:
    results = []

    results.extend(subreddits.new(**kwargs))
    results.extend(subreddits.comments(**kwargs))

    if settings['mentions']:
        results.extend(reddit.inbox.mentions(**kwargs))

    results.sort(key=lambda post: post.created_utc, reverse=True)

    return results
