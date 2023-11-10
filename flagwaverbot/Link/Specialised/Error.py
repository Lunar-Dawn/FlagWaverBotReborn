import urllib.parse

from flagwaverbot.Link import Link
from flagwaverbot.Link.is_valid_media_url import is_valid_media_url


link_template = '[{text}]({url})'


# Currently only used for Reddit galleries eating links, invalid text link still skipped to prevent spam.
class Error(Link):
    def __init__(self, url='Invalid Link'):
        super().__init__(url)

    def link_text(self, n: int) -> str:
        return f'Link #{n} failed to process'
