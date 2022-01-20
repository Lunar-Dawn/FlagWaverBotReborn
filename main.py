import logging
import time

import praw.models.util
import prawcore.exceptions

from flagwaverbot.process_item import process_item
from flagwaverbot.stream import comments_submissions_and_mentions

logging.basicConfig(format='%(asctime)s %(levelname)s - %(item_id)s - %(target_id)s: %(message)s', level=logging.INFO)


def main():
    while True:
        stream = praw.models.util.stream_generator(comments_submissions_and_mentions, skip_existing=True)
        try:
            for item in stream:
                process_item(item)
        except prawcore.exceptions.ServerError as e:
            logging.error(f'Reddit Server Error: {type(e).__name__}: {e}')
            time.sleep(10)
        except Exception as e:
            logging.error(f'General Error: {type(e).__name__}: {e}')


if __name__ == '__main__':
    main()
