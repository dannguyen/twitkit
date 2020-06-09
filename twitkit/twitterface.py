import json
from pathlib import Path
import tweepy

DEFAULT_CREDS_PATH = Path('~/.twitkitrc')

def _loadcreds(srcpath=DEFAULT_CREDS_PATH):
    return json.loads(srcpath.read_text())

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
    rawcreds = _loadcreds(srcpath)
    if username:
        uname = username.lower()
        print(uname)
        ucreds = next(d for d in rawcreds if str(d.get('username')).lower() == uname)
    else:
        ucreds = rawcreds[0]
    return ucreds



def auth_user(creds):
    pass
