from typing import Optional

import sys
import requests


def is_image(url: str) -> bool:
    image_formats = ('image/png', 'image/jpeg', 'image/jpg')

    response = get_headers(url)

    if 'content-type' not in response.headers:
        return False

    return response.headers['content-type'] in image_formats


def get_headers(url: str) -> Optional[requests.Response]:
    try:
        return requests.head(url, allow_redirects=True)
    except Exception as e:
        print(f'Error {type(e).__name__}: \'{e}\' accessing url: \'{url}\'', file=sys.stderr)
        return None
