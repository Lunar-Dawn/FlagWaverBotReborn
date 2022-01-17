import urllib.parse

from flagwaverbot.Link import Link
from flagwaverbot.Link.is_image import is_image


link_template = '[{text}]({url})'


class Image(Link):
    def __init__(self, url: str):
        super().__init__(url)

    def link_text(self, n: int) -> str:
        return link_template.format(
            text=f'Link #{n}: Image',
            url='https://krikienoid.github.io/flagwaver/#?'
                + urllib.parse.urlencode({
                    'src': 'https://flagwaver-cors-proxy.herokuapp.com/' + self.url
                })
        )

    @staticmethod
    def is_valid_url(url: str) -> bool:
        return is_image(url)
