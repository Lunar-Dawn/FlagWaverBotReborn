from typing import List

from flagwaverbot.Link import Link


class Gallery(Link):
    def __init__(self, url: str):
        super(Gallery, self).__init__(url)
        self.images: List[Link] = []

    def link_text(self, n: int) -> str:
        built_text = f'Link #{n}: Gallery\n\n'

        for i in range(0, len(self.images)):
            built_text += f'- {self.images[i].link_text(i + 1)}\n'
        built_text += '\n'

        return built_text
