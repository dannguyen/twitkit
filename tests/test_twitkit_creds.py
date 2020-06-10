from pathlib import Path

from twitkit.twitter_client import DEFAULT_CREDS_PATH, load_user_creds, _loadcreds

LOCAL_SAMPLE_PATH = Path('./sample.twitkitrc')
SAMPLE_USERNAME = 'A SAMPLE USER'

def test_default_creds_path():
    assert Path(DEFAULT_CREDS_PATH).as_posix() == '~/.twitkitrc'


def test_sample_data():
    data = _loadcreds(LOCAL_SAMPLE_PATH)
    assert len(data) == 3
    assert data[0].get('username') is None
    assert data[0].get('consumer_key') == 'defaultkey'

    assert data[1].get('username') == 'A SAMPLE USER'
    assert data[1].get('consumer_key') == 'sample_user_key'

def test_default_user_selection():
    ucreds = load_user_creds(srcpath=LOCAL_SAMPLE_PATH)
    assert ucreds['consumer_key'] == 'defaultkey'
    assert ucreds.get('username') is None

def test_load_by_username():
    ucreds = load_user_creds(srcpath=LOCAL_SAMPLE_PATH, username=SAMPLE_USERNAME)
    assert ucreds['username'] == SAMPLE_USERNAME
    assert ucreds['consumer_key'] == 'sample_user_key'
