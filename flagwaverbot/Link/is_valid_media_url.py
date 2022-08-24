from typing import Optional

import sys
import re
import requests

content_type_regex = re.compile('(image/.*)|(video/.*)')


def is_valid_media_url(url: str) -> bool:
    response = get_headers(url)

    if 'content-type' not in response.headers:
        return False

    return content_type_regex.fullmatch(response.headers['content-type']) is not None


def get_headers(url: str) -> Optional[requests.Response]:
    try:
        return requests.head(url, allow_redirects=True)
    except Exception as e:
        print(f'Error {type(e).__name__}: \'{e}\' accessing url: \'{url}\'', file=sys.stderr)
        return None
