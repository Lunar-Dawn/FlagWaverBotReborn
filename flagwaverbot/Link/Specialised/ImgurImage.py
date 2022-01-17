import re

from flagwaverbot.config import settings
from flagwaverbot.imgur import imgur
from flagwaverbot.Link.Specialised import Image

regex = re.compile(r'^(?:https?://)?(?:www\.)?imgur\.com/(\w+)/?$')


class ImgurImage(Image):
    def __init__(self, url: str):
        match = regex.fullmatch(url)

        if not match:
            raise RuntimeError('Invalid url passed to ImgurImage constructor')

        super(ImgurImage, self).__init__(imgur.get_image(match.group(1)).link)

    @staticmethod
    def is_valid_url(url: str) -> bool:
        if not settings['use_imgur']:
            return False

        return regex.fullmatch(url) is not None
