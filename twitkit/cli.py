import click
import json
from twitkit.twitface import (DEFAULT_CREDS_PATH, load_user_creds, load_twitface)

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

    myprint(creds)

@click.command()
@click.option("--credspath", default=DEFAULT_CREDS_PATH, help='the path to your creds file')
@click.option("--username", default='', help="The username in the creds file")
@click.option("--verbose", "-v", is_flag=True)
def whoami(credspath, username, verbose):

    """Authenticates with given creds and prints out info of currently authenticated user"""

    tf = load_twitface(credspath, username)
    data = tf.whoami(verbose)
    myprint(data)


cli.add_command(hello)
cli.add_command(showcreds)
cli.add_command(whoami)





## STUB STUFF

@click.command()
@click.option("--credspath", default=DEFAULT_CREDS_PATH, help='the path to your creds file')
@click.option("--username", default='', help="The username in the creds file")
@click.argument('id', nargs=1, type=click.INT)
def get_tweet(credspath, username, id):
    """quickie stub function to get a single tweet as JSON"""
    tf = load_twitface(credspath, username)
    data = tf.fetch('get_status', id=id)
    myprint(data)


@click.command()
@click.option("--credspath", default=DEFAULT_CREDS_PATH, help='the path to your creds file')
@click.option("--username", default='', help="The username in the creds file")
@click.option("--screen_name", help="The user to get favorites for; default is authenticated user")
@click.option("--count", default=5, type=click.INT, help="number of favorites to get (200 is max)")
def get_favorites(credspath, username, screen_name, count):
    """quickie stub function to get a list of favorites as JSON"""
    tf = load_twitface(credspath, username)
    if screen_name:
        data = tf.fetch('favorites', screen_name=screen_name, count=count)
    else:
        data = tf.fetch('favorites', count=count)
    myprint(data)


cli.add_command(get_tweet)
cli.add_command(get_favorites)

### END STUBS

if __name__ == '__main__':
    cli()
