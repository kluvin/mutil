def process_playlist(f, playlist):
    """Process a playlist
    Args:
        f: The function to apply to playlist entries
        playlist: The playlist to process
        *args, **kwargs: Additional arguments to be passed on to `f`
    """
    formatted_playlist = [entry.strip('\n') for entry in playlist]

    new_playlist = '\n'.join(f(entry) for entry in formatted_playlist)
    overwrite_and_reset(playlist, new_playlist)


def overwrite_and_reset(file, content):
    """Rewrite a file with `content` and then seek back to the start"""
    file.seek(0)
    file.truncate()
    file.write(content)
    file.seek(0)
