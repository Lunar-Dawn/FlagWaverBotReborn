import logging

import praw.models

from flagwaverbot.Link.Specialised import Media, Error
from flagwaverbot.Link.Specialised.Gallery import Gallery


class RedditGallery(Gallery):
    def __init__(self, submission: praw.models.Submission):
        super(RedditGallery, self).__init__(submission.url)
        self.submission = submission

        # Adapted from
        # https://www.reddit.com/r/redditdev/comments/jcc80s/how_to_get_gallery_media_in_correct_order/g90vvai/

        # Count how many images successfully process, so we don't send 10 rows of error if all fail
        successes = 0

        for item in sorted(self.submission.gallery_data['items'], key=lambda x: x['id']):
            media_id = item['media_id']
            meta = self.submission.media_metadata[media_id]
            try:
                if meta['e'] == 'Image':
                    source = meta['s']
                    self.images.append(Media(source['u']))

                    successes += 1
            except KeyError:
                self.images.append(Error())
                logging.warning(f'Reddit Gallery contains invalid entry at id {media_id}')

        if successes == 0:
            raise ValueError('Reddit gallery contains no valid images, discarding.')
