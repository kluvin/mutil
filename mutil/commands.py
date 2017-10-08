"""
mutil.commands
~~~~~~~~~~~~~~

This module contains the implementations for the commands supported by mutil.
"""

from mutil import util


def remove_playlist_duplicates(playlist):
    """Remove entries in a given playlist.
    Args:
        playlist: A file containing a playlist to check.

    Returns: The number of duplicates removed.
    """
    old_playlist = [entry.strip('\n') for entry in playlist]
    unique_entries = set(old_playlist)
    new_playlist = '\n'.join(unique_entries)
    util.overwrite_and_reset(playlist, new_playlist)

    duplicates = len(old_playlist) - len(unique_entries)
    return duplicates


def playlist_paths_use_relative(playlist, library_path):
    """Modify the playlist format to use relative paths.
    Args:
        playlist: A file-object containing a playlist to check.
        library_path: The path in which your library resides,
                      must end in a '/' and cannot contain a newline
    """
    library_path = library_path.strip()
    playlist_entries = [entry.strip('\n').strip(library_path) for entry in playlist]
    new_playlist = '\n'.join(playlist_entries)
    util.overwrite_and_reset(playlist, new_playlist)

def playlist_paths_use_absolute(playlist, library_path):
    """Modify the playlist format to use absolute paths.
    Args:
        playlist: A file-object containing a playlist to check.
        library_path: The path in which your library resides,
                      must end in a '/' and cannot contain a newline
    """
    library_path = library_path.strip()
    playlist_entries = [library_path + entry.strip('\n') for entry in playlist]
    new_playlist = '\n'.join(playlist_entries)
    util.overwrite_and_reset(playlist, new_playlist)
