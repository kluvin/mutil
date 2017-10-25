"""
mutil.commands
~~~~~~~~~~~~~~

This module contains the implementations for the commands supported by mutil.
"""


from collections import OrderedDict

from mutil import utils


def playlist_command(func, *args):
    with open(*args[0]) as playlist:
        return func(playlist, *args)


def remove_playlist_duplicates(playlist):
    """Remove entries in a given playlist.
    Args:
        playlist: A file-object containing a playlist to check.

    Returns: The number of duplicates removed.
    """
    old_playlist = [entry.strip('\n') for entry in playlist]
    unique_entries = list(OrderedDict.fromkeys(old_playlist))
    new_playlist = '\n'.join(unique_entries)
    utils.overwrite_and_reset(playlist, new_playlist)

    duplicates = len(old_playlist) - len(unique_entries)
    return duplicates


def playlist_paths_use_relative(playlist, library_path):
    """Modify the playlist format to use relative paths.
    Args:
        playlist: A file-object containing a playlist to check.
        library_path: The path in which your library resides
    """
    utils.process_playlist(lambda entry: entry.strip(library_path), playlist)


def playlist_paths_use_absolute(playlist, library_path):
    """Modify the playlist format to use absolute paths.
    Args:
        playlist: A file-object containing a playlist to check.
        library_path: The path in which your library resides, must end in a '/'.
    Raises:
        ValueError: On incorrect `library_path`
    """
    if library_path[-1:] != '/':
        raise ValueError("library_path must include a trailing slash '/'")
    utils.process_playlist(lambda entry: library_path + entry if library_path not in entry else entry, playlist)
