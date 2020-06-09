from rich.console import Console



def myprint(*args, **kwargs):
    console = Console()
    console.print(*args, **kwargs)
