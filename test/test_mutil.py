import argparse

from mutil import mutil


def test_parser_initiates(self):
    parser = mutil.init_parser()

    assert isinstance(parser, argparse.ArgumentParser)
