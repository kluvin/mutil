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


def make_remove_playlist_duplicates_action(command):
    class CustomAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            playlist_path = values[0]
            with open(playlist_path) as playlist:
                return command(playlist)
    return CustomAction


def make_playlist_path_action(command):
    class CustomAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            playlist_path = values[0]
            library_path = values[1]
            with open(playlist_path) as playlist:
                return command(playlist, library_path)
    return CustomAction


def init_parser():
    """Initiate argparse and return an `argparse.ArgumentParser`
    Returns: An `ArgumentParser`
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
      '--remove-duplicates', '-d',
      nargs=1,
      action=make_remove_playlist_duplicates_action(
        commands.remove_playlist_duplicates)
    )

    parser.add_argument(
      '--use-absolute-paths', '-A',
      nargs=2,
      action=make_playlist_path_action(
        commands.playlist_paths_use_absolute)
    )

    parser.add_argument(
      '--use-relative-paths', '-R',
      nargs=2,
      action=make_playlist_path_action(
        commands.playlist_paths_use_relative)
    )

    return parser


if __name__ == '__main__':
    main()
