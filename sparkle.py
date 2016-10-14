#!/usr/bin/env python3
"""
Welcome to Sparkle. Sparkle helps you keep track of events on your calendar.
Usage:
    sparkle (-i | --interactive)
    sparkle (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit
"""

import sys
import cmd
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class SparkleInteractive(cmd.Cmd):
    intro = 'Welcome to Sparkle.' \
        + ' Sparkle helps you keep track of events on your calendar.\n' \
        + ' (type help for a list of commands.)'
    prompt = '(Sparkle) '
    file = None

    def do_quit(self, arg):
        """
        Quits out of Interactive Mode.
        """

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    SparkleInteractive().cmdloop()
