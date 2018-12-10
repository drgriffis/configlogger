'''
Write a set of configuration options from the command line
'''

from . import writeConfig
import argparse

if __name__ == '__main__':
    def _cli():
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', nargs=2, action='append')
        parser.add_argument('-t', dest='title')
        parser.add_argument('-l', '--logfile', dest='logfile',
                help='(REQUIRED) name of file to write configuration contents to',
                default=None)
        options = parser.parse_args()
        if not options.logfile:
            parser.print_help()
            exit()
        return options

    options = _cli()
    writeConfig(
        output=options.logfile,
        settings=options.o,
        title=options.title
    )
