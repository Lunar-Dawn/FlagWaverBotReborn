from typing import List, Union

import logging
import threading

import praw.models

from flagwaverbot.Link import Link, url_to_link
from flagwaverbot.search_html import search_html
from flagwaverbot.Link.Specialised.RedditGallery import RedditGallery
from flagwaverbot.temp_attr import temp_attr


old_factory = logging.getLogRecordFactory()
log_target = threading.local()


def target_record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.target_id = getattr(log_target, 'id', '<no target>')
    return record


logging.setLogRecordFactory(target_record_factory)


class Target:
    def __init__(self, title: str, item: Union[praw.models.Comment, praw.models.Submission]):
        self.title: str = title
        self.item: Union[praw.models.Comment, praw.models.Submission] = item

        self.links: List[Link] = []

    def process(self):
        with temp_attr(log_target, 'id', self.item.fullname):
            if isinstance(self.item, praw.models.Submission):
                if hasattr(self.item, 'is_gallery'):
                    self.links = [RedditGallery(self.item)]
                elif self.item.is_self:
                    self.links = search_html(self.item.selftext_html)
                else:
                    link = url_to_link(self.item.url)
                    if link is not None:
                        self.links = [link]
            else:
                self.links = search_html(self.item.body_html)

    def reply_text(self, is_only: bool) -> str:
        with temp_attr(log_target, 'id', self.item.fullname):
            if not self.links:
                return f'There appear to be no links to images in {self.title}\n\n'
            else:
                links_text = ''
                if not is_only:
                    links_text += f'Images in {self.title}:\n\n'

                for i in range(len(self.links)):
                    links_text += self.links[i].link_text(i + 1) + '\n\n'
                return links_text
