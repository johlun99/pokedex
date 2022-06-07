import argparse
import sys

from toolbox import arg_parser


def main():
    parser = arg_parser.ArgParser(title='test', description='test')
    print(type(parser.get_attack()))


if __name__ == '__main__':
    main()
