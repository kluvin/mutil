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


class RemovePlaylistDuplicatesAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        with open(values) as playlist:
            return commands.remove_playlist_duplicates(playlist)


class PlaylistPathsUseRelative(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        playlist_path = values[0]
        library_path = values[1]
        with open(playlist_path) as playlist:
            return commands.playlist_paths_use_relative(playlist, library_path)


class PlaylistPathsUseAbsolute(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        playlist_path = values[0]
        library_path = values[1]
        with open(playlist_path) as playlist:
            return commands.playlist_paths_use_absolute(playlist, library_path)


def init_parser():
    """Initiate argparse and return an `argparse.ArgumentParser`
    Returns: An `ArgumentParser`
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
      '--remove-duplicates', '-d',
      action=RemovePlaylistDuplicatesAction)

    parser.add_argument(
      '--use-absolute-paths', '-A',
      nargs=2,
      action=PlaylistPathsUseAbsolute)

    parser.add_argument(
      '--use-relative-paths', '-R',
      nargs=2,
      action=PlaylistPathsUseRelative)

    return parser


if __name__ == '__main__':
    main()
