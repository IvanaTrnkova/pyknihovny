import click

#prikaz - click zpracuje argumenty prikazove radky a zavola puvodni funkci
@click.command()
# option je prepinac - nepovinny parametr
# jmena prepinacu zacinaji dle unixove konvence pomlckami
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
                help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello {}!'.format(name))

#toto se spusti jen kdyz pythonni program spustim primo, kdyz ho importuju, neprovede se
if __name__ == '__main__':
    hello()