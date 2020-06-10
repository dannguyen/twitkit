import click
import json
from twitkit.twitter_client import (auth_api, DEFAULT_CREDS_PATH, load_user_creds,
    SIMPLFIED_USER_ATTRS, SIMPLIFIED_TWEET_ATTRS)

from twitkit.utils import myprint

@click.group()
def cli():
    pass


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="What's your name", help="a hello Click example")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")



@click.command()
@click.option("--credspath", default=DEFAULT_CREDS_PATH, help='the path to your creds file')
@click.option("--username", default='', help="The username in the creds file")
def showcreds(credspath, username):
    """Tells you where the creds are coming form"""
    _dname = f"'{username}'" if username else '<DEFAULT USERNAME>'
    myprint(f"Pulling username [bold cyan]{_dname}[/bold cyan] creds",
            f"from [bold green]{credspath}[/bold green]")
    creds = load_user_creds(credspath, username)
    # censor logs
    creds = creds.copy()
    for k in ('consumer_key', 'consumer_secret', 'access_token', 'access_token_secret'):
        creds[k] = creds[k][0:4] + '---REDACTED---'

    myprint(f"{json.dumps(creds, indent=2)}")




@click.command()
@click.option("--credspath", default=DEFAULT_CREDS_PATH, help='the path to your creds file')
@click.option("--username", default='', help="The username in the creds file")
@click.option("--verbose", "-v", is_flag=True)
def whoami(credspath, username, verbose):
    creds = load_user_creds(credspath, username)
    client = auth_api(creds)
    data = client.me()._json

    if verbose:
        me = data
    else:
        me =  {k: v for k, v in data.items() if k in SIMPLFIED_USER_ATTRS }
        if data.get('status'):
            _t = data['status']
            me['latest_tweet'] = {k: v for k, v in _t.items() if k in SIMPLIFIED_TWEET_ATTRS }



    myprint(f"{json.dumps(me, indent=2)}")


cli.add_command(hello)
cli.add_command(showcreds)
cli.add_command(whoami)


if __name__ == '__main__':
    cli()
