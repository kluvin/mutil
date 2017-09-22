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
      '--remove-duplicates', '-d',
      action=commands.RemovePlaylistDuplicatesAction)

    parser.add_argument(
      '--use-absolute-paths', '-A',
      nargs=2,
      action=commands.PlaylistPathsUseAbsolute)

    parser.add_argument(
      '--use-relative-paths', '-R',
      nargs=2,
      action=commands.PlaylistPathsUseRelative)

    return parser


if __name__ == '__main__':
    main()
