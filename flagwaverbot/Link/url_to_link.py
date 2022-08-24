from typing import Optional

import logging

from flagwaverbot.Link import Link
from flagwaverbot.Link.Specialised import Media, ImgurMedia, ImgurAlbum, ImgurGallery


def url_to_link(url: str) -> Optional[Link]:
    try:
        if ImgurMedia.is_valid_url(url):
            return ImgurMedia(url)

        if ImgurAlbum.is_valid_url(url):
            return ImgurAlbum(url)

        if ImgurGallery.is_valid_url(url):
            return ImgurGallery(url)

        if Media.is_valid_url(url):
            return Media(url)

    except Exception as e:
        logging.warning(f'Exception {type(e).__name__} converting from url {url} to specialised Link: {e}')
    return None
