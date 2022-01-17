from typing import List, Union

import logging
import re
import threading

import praw.models

from flagwaverbot.bot import reddit
from flagwaverbot.config import settings
from flagwaverbot.Target import Target
from flagwaverbot.temp_attr import temp_attr

comment_template = (
    f'{{body}}\n\n'
    f'*****\n\n'
    f'Beep Boop I\'m a bot. [About]({settings["about_link"]}). Maintained by {settings["maintainer"]}'
)
working_template = 'Here you go:\n\n {links}'
error_template = (
    f'Something appears to be wrong with the link requested or the bot.\n\n'
    f'Please [report]({settings["error_link"]}) this. Summoner id: {{id}}'
)

old_factory = logging.getLogRecordFactory()
local_item_id = threading.local()


def item_record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.item_id = getattr(local_item_id, 'item_id', '<no caller>')
    return record


logging.setLogRecordFactory(item_record_factory)


def process_item(item: Union[praw.models.Comment, praw.models.Submission]):
    with temp_attr(local_item_id, 'item_id', item.fullname):
        try:
            if item.author == reddit.user.me():
                return

            if isinstance(item, praw.models.Submission) and not item.is_self:
                return

            targets = get_targets(item)
            if not targets:
                return

            logging.info(f'Summoned to process links in {", ".join([t.item.fullname for t in targets])}')

            for target in targets:
                target.process()

            if not settings['reply_empty_summon']:
                num_valid = sum(1 for t in targets if t.links)

                if num_valid == 0:
                    return

            reply_text = comment_template.format(
                body=working_template.format(
                    links='*****\n\n'.join(map(lambda t: t.reply_text(is_only=len(targets) == 1), targets))
                )
            )
        except Exception as e:
            logging.warning(f'Error processing summon: {type(e).__name__}: {e}')

            reply_text = comment_template.format(
                body=error_template.format(
                    id=item.fullname
                )
            )

        try:
            item.reply(reply_text)
        except Exception as e:
            logging.error(f'Could not respond to summon: {type(e).__name__}: {e}')


# Get the comment(s) and/or submission to scrape for links
def get_targets(item: Union[praw.models.Comment, praw.models.Submission]) -> List[Target]:
    targets = []
    if isinstance(item, praw.models.Comment):
        if settings['allow_reply'] and re.search(r'(?<!\w)!wave(?!\w)', item.body):
            if item.is_root:
                targets.append(Target('the parent post', item.submission))
            else:
                targets.append(Target('the parent comment', item.parent()))

        if settings['allow_self'] and re.search(r'(?<!\w)!wavethis(?!\w)', item.body):
            targets.append(Target(f'your comment', item))
    else:
        if settings['allow_self'] and re.search(r'(?<!\w)!wavethis(?!\w)', item.selftext):
            targets.append(Target(f'your post', item))

    return targets
