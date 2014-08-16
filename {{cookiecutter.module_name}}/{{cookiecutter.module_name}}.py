# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '0.1.0'

{% if cookiecutter.console_script_name != "" %}
import click
{% endif %}

######################################
#
# Your code goes here
#
######################################

{% if cookiecutter.console_script_name != "" %}
@click.command()
# See instructions at http://click.pocoo.org/
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
def main():
    """This function should merely process arguments and options
        received from the command-line into your snippet of code.
    """
    raise NotImplementedError("Add calling code to main() function")

if __name__ == '__main__':
    main()
{% endif %}