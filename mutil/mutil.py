"""
mutil.mutil
~~~~~~~~~~~

This module implements the logic for enabling command-line usage.
"""

import argparse

from mutil import commands


def main():
    parser = init_parser()
    parser.parse_args()


def init_parser():
    """Initiate argparse and return an `argparse.ArgumentParser`
    Returns: An `ArgumentParser`
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
      '--remove-duplicates', '-rd',
      action=commands.RemovePlaylistDuplicatesAction)

    parser.add_argument(
      '--toggle-format', '-tf',
      nargs=2,
      action=commands.TogglePlaylistPathFormat)

    return parser


if __name__ == '__main__':
    main()
