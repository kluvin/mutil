import argparse

from mutil import commands


def main():
    parser = init_parser()
    parser.parse_args()


def init_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
    '--remove-duplicates', '-rd',
    action=commands.RemovePlaylistDuplicatesAction)

    return parser


if __name__ == '__main__':
    main()