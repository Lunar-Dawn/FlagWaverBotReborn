from typing import Optional

import pyimgur

from flagwaverbot.config import settings, secret

imgur: Optional[pyimgur.Imgur] = None
if settings['use_imgur']:
    imgur = pyimgur.Imgur(secret['Imgur']['client_id'])
