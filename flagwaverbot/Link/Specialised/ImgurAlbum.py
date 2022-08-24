import re

from flagwaverbot.config import settings
from flagwaverbot.imgur import imgur
from flagwaverbot.Link.Specialised import Media
from flagwaverbot.Link.Specialised.Gallery import Gallery

regex = re.compile(r'^(?:https?://)?(?:www\.)?imgur\.com/a/(\w+)/?$')


class ImgurAlbum(Gallery):
    def __init__(self, url: str):
        super(ImgurAlbum, self).__init__(url)

        match = regex.fullmatch(url)

        if not match:
            raise RuntimeError('Invalid url passed to ImgurGallery constructor')

        album = imgur.get_album(match.group(1))

        self.images = [Media(i.link) for i in album.images]

    @staticmethod
    def is_valid_url(url: str) -> bool:
        if not settings['use_imgur']:
            return False

        return regex.fullmatch(url) is not None
