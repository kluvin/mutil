import argparse

from mutil import api


def test_parser_initiates():
    parser = api.init_parser()

    assert isinstance(parser, argparse.ArgumentParser)
