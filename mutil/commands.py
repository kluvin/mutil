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
