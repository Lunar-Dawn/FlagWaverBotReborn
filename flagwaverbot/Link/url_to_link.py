from typing import Optional

import logging

from flagwaverbot.Link import Link
from flagwaverbot.Link.Specialised import Image, ImgurImage, ImgurAlbum


def url_to_link(url: str) -> Optional[Link]:
    try:
        if ImgurImage.is_valid_url(url):
            return ImgurImage(url)

        if ImgurAlbum.is_valid_url(url):
            return ImgurAlbum(url)

        if Image.is_valid_url(url):
            return Image(url)

    except Exception as e:
        logging.warning(f'Exception {type(e).__name__} converting from url {url} to specialised Link: {e}')
    return None
