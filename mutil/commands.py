"""
mutil.commands
~~~~~~~~~~~~~~

This module contains the implementations for the commands supported by mutil.
"""

import argparse


class RemovePlaylistDuplicatesAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        with open(values) as playlist:
            return remove_playlist_duplicates(playlist)


class TogglePlaylistPathFormat(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        playlist_path = values[0]
        library_path = values[1]
        with open(playlist_path) as playlist:
            return toggle_playlist_path_format(playlist, library_path)


def remove_playlist_duplicates(playlist):
    """Remove entries in a given playlist.
    Args:
        playlist: A file containing a playlist to check.

    Returns: The number of duplicates removed.
    """
    playlist_entries = []
    duplicates = 0
    for entry in playlist:
        entry = entry.strip('\n')
        if entry in playlist_entries:
            duplicates += 1
        else:
            playlist_entries.append(entry)
    new_playlist = '\n'.join(playlist_entries)

    # Overwrite the old playlist
    playlist.seek(0)
    playlist.truncate()
    playlist.write(new_playlist)
    playlist.seek(0)

    return duplicates


def toggle_playlist_path_format(playlist, library_path):
    """Modify the playlist format to use either relative or absolute
       paths.
    Args:
        playlist: A file-object containing a playlist to check.
        library_path: The path in which your library resides,
                      must end in a '/' and cannot contain a newline
    """
    library_path = library_path.strip()
    playlist_entries = []
    for entry in playlist:
        entry = entry.strip('\n')
        # Is absolute, change to relative
        if entry.startswith(library_path):
            entry = entry.strip(library_path)
        # Is relative, change to absolute
        else:
            entry = library_path + entry
        playlist_entries.append(entry)

    new_playlist = '\n'.join(playlist_entries)

    # Overwrite the old playlist
    playlist.seek(0)
    playlist.truncate()
    playlist.write(new_playlist)
    playlist.seek(0)
