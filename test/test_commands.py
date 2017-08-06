import doubles

from context import mutil
from mutil import commands


def mock_open(file, return_value):
    from io import StringIO
    import builtins

    doubles.allow(builtins).open.with_args(file).and_return(StringIO(return_value))


def test_correctly_removes_duplicates_when_present():
    expected = ['bad/duplicated/album', 'random/good/entry']
    expected = '\n'.join(expected
                         )
    duplicated = ['bad/duplicated/album', 'random/good/entry', 'bad/duplicated/album']
    duplicated = '\n'.join(duplicated)

    mock_open('./bad_playlist.m3u8', duplicated)

    bad_playlist = open('./bad_playlist.m3u8')

    duplicates = commands.remove_playlist_duplicates(bad_playlist)

    assert bad_playlist.read() == expected
    assert duplicates == 1

def test_does_not_modify_unduplicated_playlist():
    expected = ['good/unduped/playlist', 'another/good/entry', 'last/entry']
    expected = '\n'.join(expected
                         )
    playlist = ['good/unduped/playlist', 'another/good/entry', 'last/entry']
    playlist = '\n'.join(playlist)

    mock_open('./bad_playlist.m3u8', playlist)

    bad_playlist = open('./bad_playlist.m3u8')

    duplicates = commands.remove_playlist_duplicates(bad_playlist)

    assert bad_playlist.read() == expected
    assert duplicates == 0