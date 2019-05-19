# import click
# import time
# import datetime

# @click.command()
# @click.option('--gender', type=click.Choice(['man', 'woman']))    # 限定值
# def choose(gender):
#     t = datetime.datetime.now()    
#     click.echo('gender: %s' % gender)
#     elapsed = (datetime.datetime.now() - t).total_seconds()
#     print(elapsed)
# if __name__ == '__main__':
#     choose()
    

import click

@click.command()
@click.option('--name', help='The person to greet.')
def hello(name):
    click.secho('Hello %s!' % name, fg='blue', underline=False)
    click.secho('Hello %s!' % name, fg='yellow', bg='black')

if __name__ == '__main__':
    hello(name)