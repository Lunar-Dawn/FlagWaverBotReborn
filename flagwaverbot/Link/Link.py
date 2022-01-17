class Link:
    def __init__(self, url: str):
        self.url = url

    def __repr__(self):
        return self.url

    def link_text(self, n: int) -> str:
        raise NotImplementedError('Link type response not implemented')

    @staticmethod
    def is_valid_url(url: str) -> bool:
        return False
