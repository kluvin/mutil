from subprocess import run
import os

def test_mutil_displays_help_message():
    os.chdir('../')

    run('python -m mutil.api -h'.split(' '), check=True)

def test_mutil_runs_custom_command():
    os.chdir('../')

    with open('playlist.txt', 'w') as playlist:
        playlist.write('a\na\na')
    run('python -m mutil.api -d playlist.txt'.split(' '), check=True)
