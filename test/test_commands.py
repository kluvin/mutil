import doubles

from context import mutil
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


def test_duplicated_playlist_behaves_as_expected():
    my_playlist = to_string(['bad/duplicated/album', 'random/good/entry', 'bad/duplicated/album'])
    expected_playlist = to_string(['bad/duplicated/album', 'random/good/entry'])

    mock_open('a_playlist.m3u8', my_playlist)

    my_playlist = open('a_playlist.m3u8')
    duplicates = commands.remove_playlist_duplicates(my_playlist)

    assert duplicates == 1
    assert my_playlist.read() == expected_playlist


def test_non_duplicated_playlist_behaves_as_expected():
    my_playlist = to_string(['good/non-duped/album', 'another/good/entry', 'last/entry'])
    expected_playlist = to_string(['good/non-duped/album', 'another/good/entry', 'last/entry'])

    mock_open('a_playlist.m3u8', my_playlist)

    my_playlist = open('a_playlist.m3u8')
    duplicates = commands.remove_playlist_duplicates(my_playlist)

    assert duplicates == 0
    assert my_playlist.read() == expected_playlist
