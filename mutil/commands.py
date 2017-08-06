def remove_playlist_duplicates(playlist):
    """Removes entries in a given playlist.
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