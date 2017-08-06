import doubles

from context import mutil
from mutil import commands


def mock_open(file, return_value):
    from io import StringIO
    import builtins

    doubles.allow(builtins).open.with_args(file).and_return(StringIO(return_value))


def test_correctly_removes_duplicates_when_present():
    mock_open('./bad_playlist.m3u8', '''bad/duplicated/album\n
                                        random/good/entry\n
                                        bad/duplicated/album
                                        ''')
    mock_open('./good_playlist.m3u8)', '''good/unduped/album\n
                                          another/entry/here\n
                                          can/we/have/another?
                                          ''')

    bad_playlist = open('./bad_playlist.m3u8')
    good_playlist = open('./good_playlist.m3u8')

    processed_playlist = commands.remove_playlist_duplicates(bad_playlist)

    assert processed_playlist == good_playlist


def test_does_not_modify_unduplicated_playlist():
    mock_open('./bad_playlist.m3u8',   '''bad/duplicated/album\n
                                          random/good/entry\n
                                          bad/duplicated/album
                                          ''')
    mock_open('./good_playlist.m3u8', '''good/unduped/album\n
                                          another/entry/here\n
                                          can/we/have/another?
                                          ''')

    bad_playlist = open('./bad_playlist.m3u8')
    good_playlist = open('./good_playlist.m3u8')

    processed_playlist = commands.remove_playlist_duplicates(bad_playlist)

    assert processed_playlist == good_playlist
