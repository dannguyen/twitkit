import json
from pathlib import Path
import tweepy

DEFAULT_CREDS_PATH = Path('~/.twitkitrc')


def load_user_creds(srcpath=DEFAULT_CREDS_PATH, username=None):
    """
    srcpath <string>: points to a JSON file, with a list of dicts
    username <string>: specifies which user creds to use; if None, returns
        first

    Returns <dict>: a dict that looks like:

        {
          "consumer_key": "some_consumer_key",
          "consumer_secret": "theconsumerSecret",
          "access_token": "999999-accesstoken",
          "access_token_secret": "asdfsecrettoken"
        }
    """
    srcpath = Path(srcpath).expanduser().absolute()
    data = json.loads(srcpath.read_text())
    if username:
        creds = next(d for d in data if d['username'] == username.lower())
    else:
        creds = data[0]
    return creds



def auth_user(creds):
