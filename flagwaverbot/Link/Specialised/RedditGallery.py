import praw.models

from flagwaverbot.Link.Specialised import Image
from flagwaverbot.Link.Specialised.Gallery import Gallery


class RedditGallery(Gallery):
    def __init__(self, submission: praw.models.Submission):
        super(RedditGallery, self).__init__(submission.url)
        self.submission = submission

        # Adapted from
        # https://www.reddit.com/r/redditdev/comments/jcc80s/how_to_get_gallery_media_in_correct_order/g90vvai/

        for item in sorted(self.submission.gallery_data['items'], key=lambda x: x['id']):
            media_id = item['media_id']
            meta = self.submission.media_metadata[media_id]
            if meta['e'] == 'Image':
                source = meta['s']
                self.images.append(Image(source['u']))
