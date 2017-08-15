import doubles

from mutil import commands


def mock_open(file, return_value):
    """Mock the open filesystem call
    Args:
        file: The file to mock; equivalent to first arg of open()
        return_value: The value
    """
    from io import StringIO
    import builtins

    doubles.allow(builtins).open.with_args(file).and_return(StringIO(return_value))


def to_string(content):
    return '\n'.join(content)


class TestRemovePlaylistDuplicates:
    def test_duplicated_playlist_behaves_as_expected(self):
        my_playlist = to_string(['bad/duplicated/album', 'random/good/entry', 'bad/duplicated/album'])
        expected_playlist = to_string(['bad/duplicated/album', 'random/good/entry'])

        mock_open('a_playlist.m3u8', my_playlist)

        my_playlist = open('a_playlist.m3u8')
        duplicates = commands.remove_playlist_duplicates(my_playlist)

        assert duplicates == 1
        assert my_playlist.read() == expected_playlist

    def test_non_duplicated_playlist_behaves_as_expected(self):
        my_playlist = to_string(['good/non-duped/album', 'another/good/entry', 'last/entry'])
        expected_playlist = to_string(['good/non-duped/album', 'another/good/entry', 'last/entry'])

        mock_open('a_playlist.m3u8', my_playlist)

        my_playlist = open('a_playlist.m3u8')
        duplicates = commands.remove_playlist_duplicates(my_playlist)

        assert duplicates == 0
        assert my_playlist.read() == expected_playlist


class TestTogglePlaylistPathFormat:
    def test_correctly_toggles_absolute_format_to_relative(self):
        expected_playlist = 'album/track'
        library_path = '/home/$USER/Music/\n'
        mock_open('a_playlist', '/home/$USER/Music/album/track\n')
        my_playlist = open('a_playlist')

        commands.toggle_playlist_path_format(my_playlist, library_path)

        assert my_playlist.read() == expected_playlist

    def test_correctly_toggles_relative_format_to_absolute(self):
        expected_playlist = '/home/$USER/Music/album/track'
        library_path = '/home/$USER/Music/\n'
        mock_open('a_playlist', 'album/track\n')
        my_playlist = open('a_playlist')

        commands.toggle_playlist_path_format(my_playlist, library_path)

        assert my_playlist.read() == expected_playlist
