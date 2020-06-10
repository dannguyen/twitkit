import json
from pathlib import Path
import tweepy

DEFAULT_CREDS_PATH = Path('~/.twitkitrc')
SIMPLFIED_USER_ATTRS = ('id', 'screen_name', 'name', 'description',
                        'followers_count', 'friends_count', 'statuses_count',
                        'favourites_count', 'created_at',)

SIMPLIFIED_TWEET_ATTRS = ('id', 'created_at', 'text', 'retweet_count', 'favorite_count', 'in_reply_to_screen_name')

def _loadcreds(srcpath=DEFAULT_CREDS_PATH):
    return json.loads(srcpath.read_text())

def load_user_creds(srcpath=DEFAULT_CREDS_PATH, username=None):
    """
    srcpath <string>: points to a JSON file, with a list of dicts
    username <string>: specifies which user creds to use; if None, returns
        first

    Returns: <dict> something that looks like:

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




def auth_api(creds):
    """
    creds <dict>: a dict of strings, e.g.

        {
          "consumer_key": "some_consumer_key",
          "consumer_secret": "theconsumerSecret",
          "access_token": "999999-accesstoken",
          "access_token_secret": "asdfsecrettoken"
        }

    Returns: tweepy.api.API
    """
    auth = tweepy.OAuthHandler(consumer_key=creds['consumer_key'],
                               consumer_secret=creds['consumer_secret'])
    auth.set_access_token(creds['access_token'],
                      creds['access_token_secret'])

    return tweepy.API(auth, wait_on_rate_limit_notify=True,
                            wait_on_rate_limit=True)

