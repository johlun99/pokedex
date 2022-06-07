import argparse


class ArgParser:
    def __init__(self, title='', description=''):
        parser = argparse.ArgumentParser(prog=title,
                                         description=description)

        wildcards = parser.add_argument_group('Wildcards')
        flags = parser.add_argument_group('Flags')

        wildcards.add_argument('--all',
                               help='Retrieve datadump of all pokemon (crazy bastard o.O)',
                               action='store_true')

        flags.add_argument('-a', '--attack',
                           help="Retrieves the attack of the given pokemon",
                           action='store_true')

        self.args = parser.parse_args()

    def get_attack(self):
        return self.args.attack
