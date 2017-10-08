import pyfakefs
import pytest

from mutil import commands, util


@pytest.fixture
def playlist(fs):
    """Open a fake file object
    Args:
        fs: A reference to the `pyfakefs` filesystem
    """
    fs.CreateFile('playlist')
    with open('playlist', 'r+') as playlist:
        yield playlist


class TestRemovePlaylistDuplicates:
    def test_duplicates_are_removed(self, playlist):
        playlist.write(util.list_to_string(['a/b/c', 'a/b/c', '1/2/3']))
        playlist.seek(0)
        expectation = ['a/b/c', '1/2/3']

        duplicates = commands.remove_playlist_duplicates(playlist)

        reality = [entry.strip('\n') for entry in playlist]
        assert duplicates == 1
        assert sorted(expectation) == sorted(reality)

    def test_non_duplicated_playlist_behaves_as_expected(self, playlist):
        playlist.write(util.list_to_string(['a/b/c', '1/2/3']))
        playlist.seek(0)
        expected = util.list_to_string(['a/b/c', '1/2/3'])

        duplicates = commands.remove_playlist_duplicates(playlist)

        assert duplicates == 0
        assert playlist.read() == expected

    def test_empty_playlist(self, playlist):
        playlist.write(util.list_to_string([]))
        playlist.seek(0)
        expectation = util.list_to_string([])

        duplicates = commands.remove_playlist_duplicates(playlist)
        reality = playlist.read()

        assert duplicates == 0
        assert sorted(expectation) == sorted(reality)

    def test_invalid_playlist(self, playlist):
        playlist.write(util.list_to_string(['my\nplaylist']))
        playlist.seek(0)
        expectation = util.list_to_string(['my\nplaylist'])

        duplicates = commands.remove_playlist_duplicates(playlist)
        reality = playlist.read()

        assert duplicates == 0
        assert sorted(expectation) == sorted(reality)


class TestPlaylistPathsUseRelative:
    def test_correctly_toggles_absolute_format_to_relative(self, playlist):
        playlist.write('/home/$USER/Music/album/track\n')
        playlist.seek(0)
        expected_playlist = 'album/track'
        library_path = '/home/$USER/Music/\n'

        commands.playlist_paths_use_relative(playlist, library_path)

        assert playlist.read() == expected_playlist

    def test_relative_playlist_remains_relative(self, playlist):
        playlist.write('album/track\n')
        playlist.seek(0)
        expected_playlist = 'album/track'
        library_path = '/home/$USER/Music/\n'

        commands.playlist_paths_use_relative(playlist, library_path)

        assert playlist.read() == expected_playlist

class TestPlaylistPathsUseAbsolute:
    def test_correctly_toggles_relative_format_to_absolute(self, playlist):
        expected_playlist = '/home/$USER/Music/album/track'
        library_path = '/home/$USER/Music/\n'
        playlist.write('album/track\n')
        playlist.seek(0)

        commands.playlist_paths_use_absolute(playlist, library_path)

        assert playlist.read() == expected_playlist

    # ToDo; Implement
    # def test_absolute_playlist_remains_absolute(self, playlist):
    #     expected_playlist = '/home/$USER/Music/album/track'
    #     library_path = '/home/$USER/Music/\n'
    #     playlist.write('/home/$USER/Music/album/track\n')
    #     playlist.seek(0)
    #
    #     commands.playlist_paths_use_absolute(playlist, library_path)
    #
    #     assert playlist.read() == expected_playlist