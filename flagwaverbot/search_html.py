from typing import List

from bs4 import BeautifulSoup

from flagwaverbot.Link import Link, url_to_link


def search_html(html: str) -> List[Link]:
    links = []

    soup = BeautifulSoup(html, 'html.parser')

    for a_tag in soup.find_all('a'):
        raw_link = a_tag.get("href")
        link = url_to_link(raw_link)

        if link is not None:
            links.append(link)

    return links
