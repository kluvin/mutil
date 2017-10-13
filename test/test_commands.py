import pyfakefs
import pytest

from mutil import commands, util


@pytest.fixture
def playlist(fs):
    # noinspection SpellCheckingInspection
    """Open a fake file object
        Args:
            fs: A reference to the `pyfakefs` filesystem
        """
    fs.CreateFile('playlist')
    with open('playlist', 'r+') as playlist:
        yield playlist


@pytest.mark.parametrize('test_input, expectation, duplicates_expected', [
    ('a/b/c\na/b/c\n1/2/3', 'a/b/c\n1/2/3', 1),  # Duplicated
    ('a/b/c\n1/2/3', 'a/b/c\n1/2/3', 0),         # Non-duplicated
    ('', '', 0),                                 # Empty
])
def test_remove_playlist_duplicates(playlist, test_input, expectation, duplicates_expected):
    util.write_and_reset(playlist, test_input)

    duplicates_found = commands.remove_playlist_duplicates(playlist)

    reality = playlist.read()
    assert duplicates_expected == duplicates_found
    assert expectation == reality


class TestPlaylistPathCommands:
    library_path = '/home/$USER/Music/'
    library_path_w_trailing_slash = library_path + '/'
    absolute_path = '/home/$USER/Music/album/track'
    relative_path = 'album/track'

    @pytest.mark.parametrize('test_input, expectation', [
        (absolute_path, relative_path),  # Absolute to relative
        (relative_path, relative_path)   # Relative to relative
    ])
    @pytest.mark.parametrize('library_path', [library_path, library_path_w_trailing_slash])
    def test_playlist_paths_use_relative(self, playlist, test_input, expectation, library_path):
        util.write_and_reset(playlist, test_input)

        commands.playlist_paths_use_relative(playlist, library_path)

        reality = playlist.read()
        assert expectation == reality

    @pytest.mark.parametrize('test_input, expectation', [
        (relative_path, absolute_path),  # Relative to absolute
        (absolute_path, absolute_path)   # Absolute to absolute
    ])
    def test_playlist_paths_use_absolute(self, playlist, test_input, expectation):
        util.write_and_reset(playlist, test_input)

        commands.playlist_paths_use_absolute(playlist, self.library_path)

        reality = playlist.read()
        assert expectation == reality
