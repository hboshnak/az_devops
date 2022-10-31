"""Module demonstrating Click 
"""
import click

@click.command(help="This is a Click example app.")
@click.option("--name", prompt="Name to be defined", help="I need a name")
@click.option("--color", prompt="Color to be defined", help="I need a color")
def main(name, color):
    """Basic Click example
    """
    if name == "Mani":
        click.echo("Mani, you are always black!")
        click.echo(click.style(f"Hello {name}!", fg="black"))
    else:
        click.echo(f"Your color of choise is {color}!")
        click.echo(click.style(f"Hello {name}!", fg=color))

if __name__ == "__main__":
    main()