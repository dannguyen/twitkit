import click
import json
from twitkit.twitterface import DEFAULT_CREDS_PATH, load_user_creds
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
    myprint(f"{json.dumps(creds, indent=2)}")



cli.add_command(hello)
cli.add_command(showcreds)



if __name__ == '__main__':
    cli()
