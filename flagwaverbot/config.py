import sys

from strictyaml import load, Map, Str, UniqueSeq, YAMLError, Bool
from path import Path

try:
    settings = load(Path('settings.yaml').read_text(),
                    Map({
                        'user_agent': Str(),
                        'subreddits': UniqueSeq(Str()),
                        'allow_self': Bool(),
                        'allow_reply': Bool(),
                        'mentions': Bool(),

                        'about_link': Str(),
                        'error_link': Str(),
                        'maintainer': Str(),

                        'cors_proxy': Str(),

                        'use_imgur': Bool(),

                        'reply_empty_summon': Bool(),
                    }),
                    label='settings.yaml'
                    ).data

    secret = load(Path('secret.yaml').read_text(),
                  Map({
                      'Reddit': Map({
                          'client_id': Str(),
                          'client_secret': Str(),

                          'username': Str(),
                          'password': Str(),
                      }),
                      'Imgur': Map({
                          'client_id': Str(),
                      }),
                  }),
                  label='secret.yaml'
                  ).data

except YAMLError as error:
    print(f'Error reading configuration:\n{error}', file=sys.stderr)
    exit(1)
