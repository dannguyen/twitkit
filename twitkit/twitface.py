import json
from pathlib import Path
import tweepy
from tweepy.models import Model as tweepBaseModel
from tweepy import TweepError

DEFAULT_CREDS_PATH = Path('~/.twitkitrc')
SIMPLFIED_USER_ATTRS = ('id', 'screen_name', 'name', 'description',
                        'followers_count', 'friends_count', 'statuses_count',
                        'favourites_count', 'created_at',)

SIMPLIFIED_TWEET_ATTRS = ('id', 'created_at', 'text', 'retweet_count', 'favorite_count', 'in_reply_to_screen_name')



"""
from twitkit.twitface import load_twitface; tf = load_twitface()
"""


class TwitFace:
    """
    A class that wraps around Tweepy API
    """
    def __init__(self, creds=None):
        self.creds = creds
        self.api = None
        self._cache = {}

        if creds:
            self.auth_api(creds) # set self.api


    def is_auth(self):
        return type(self.api) is tweepy.api.API

    def auth_api(self, creds):
        self.api = _auth_api_with_creds(creds)
        return self.api

    def dcache(self, key=None, value='__GETTER_BY_DEFAULT__'):
        """
        :key <str>: a key in the _cache dict
        :value <str>, <dict>, <None>, or subclass of <tweepBaseModel>:
            if: '__GETTER_BY_DEFAULT__', i.e. not set by user, we assume user wants to get a value
            else: we assume user wants to wants to set value of _cache[key]

                if :value is not a <tweepBaseModel> or <None> or <dict>, a ValueError is thrown
        Returns:
            <dict> if getting _cache[:key] or if _cache[:key] = value is successful, and value is
                subclass of tweepBaseModel

            <NoneType> if getting _cache[:key] was unsuccessful

        TK: WHAT IS EVEN THE POINT OF ALL THIS??
        """
        if key is None:
            return d._cache.copy()

        if value == '__GETTER_BY_DEFAULT__':
            # just doing getter
            val = self._cache.get(key)
        else:
            # attempting a setter
            val = _convert_tweepy_model(value)
            if type(val) in (dict, list, type(None)):
                self._cache[key] = val
            else:
                raise ValueError(f"Expected :value to be either dict, list, oneType, or tweepy.models.Model/ResultSet, but got {type(value)} instead: {value}")


        return val.copy() if type(val) in (dict, list) else val


    def fetch(self, endpoint, as_dict=True, **kwargs):
        """
        :endpoint <str>: a tweepy endpoint name, like 'me', or 'followers', or 'get_user'

        :as_json <bool>: if True,

        Returns:
            <dict> if :as_dict is True
            <tweepy.models.Model> if :as_dict is not True
        """

        apifoo = getattr(self.api, endpoint)
        data = apifoo(**kwargs)
        if as_dict is True:
            return _convert_tweepy_model(data)
        else:
            return data


    def batch_unlike(self, ids):
        """
        ids <list>: a list of twitter IDs, ostensibly one that can fit in memory

        Returns <list of dicts>:
        """

        results = []
        for i in ids:
            idval = str(i)
            d = self.fetch('destroy_favorite', as_dict=True, id=idval)
            results.append(d)
        return results


    def whoami(self, verbose=False):
        me = self.dcache('whoami')
        if not me:
            tdata = self.fetch('me', as_dict=True)
            me = self.dcache('whoami', tdata)


        if verbose:
            whome = me
        else:
            whome =  {k: v for k, v in me.items() if k in SIMPLFIED_USER_ATTRS }
            if me.get('status'):
                _tweet = me['status']
                whome['latest_tweet'] = {k: v for k, v in _tweet.items() if k in SIMPLIFIED_TWEET_ATTRS }

        return whome





### helper methods


def _auth_api_with_creds(creds):
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



def _convert_tweepy_model(records, CONCISE_MODEL_TBD=None):
    """
    CONCISE_MODEL_TBD: returns EasyDatum when possible

    :records
        <tweepy.models.ResultSet>: basically, a list of tweepy models
        <tweepy.models.Model>: any subclass of models

    Returns:
        <list> if :records was a ResultSet
        <dict> if :records was a single Model
        <other> simply returns whatever :records is
    """
    if issubclass(type(records), tweepy.models.ResultSet):
        data = [r._json for r in records]
    elif issubclass(type(records), tweepy.models.Model):
        data = records._json
    else:
        # raise ValueError(f":records was expected to be tweepy.models.ResultSet or tweepy.models.Model; got {type(records)} instead")
        data = records
    return data


def _loadcreds(credspath=DEFAULT_CREDS_PATH):
    return json.loads(credspath.read_text())

def load_user_creds(credspath=DEFAULT_CREDS_PATH, username=None):
    """
    :credspath <string>: points to a JSON file, with a list of dicts
    :username <string>: specifies which user creds to use; if None, returns
        first

    Returns: <dict>
        Something that looks like:

        {
          "consumer_key": "some_consumer_key",
          "consumer_secret": "theconsumerSecret",
          "access_token": "999999-accesstoken",
          "access_token_secret": "asdfsecrettoken"
        }
    """
    credspath = Path(credspath).expanduser().absolute()
    rawcreds = _loadcreds(credspath)
    if username:
        uname = username.lower()
        print(uname)
        ucreds = next(d for d in rawcreds if str(d.get('username')).lower() == uname)
    else:
        ucreds = rawcreds[0]
    return ucreds


def load_twitface(credspath=DEFAULT_CREDS_PATH, username=None):
    """
    convenience function that instantiates a TwitFace given a credspath and username
    """
    return TwitFace(load_user_creds(credspath, username))


