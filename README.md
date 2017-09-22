# mutil - Music Utilities

**mutil** is a command-line program to manage your music collection.

## Usage

Three commands are currently supported, they are (and can be invoked) as follows:

* **Remove playlist duplicates**, long form: `--remove-duplicates`; short form `-d`
* **Use absolute playlist paths**, long form: `--use-absolute-paths`; short form `-A`
* **Use Relative playlist paths**, long form: `--use-relative-paths`; short form `-R`
* **Help**, long form: `--help`; short form `-h`

## Design and Development

You can find some block comments spread throughout the source (`test_commands`, `mutil`, and `commands`) in the code-review branch.

* The `*Action` classes take values handed to us by `argparse` and feeds them into the class' corresponding function.
* Tests were written before the code, TDD style, although the code quality may not reflect this ;) Admittedly I didn't do so religiously, I just wrote the tests before I wrote the code, simply put.
* Tests are supposed to follow the [Arrange-Act-Assert pattern](http://wiki.c2.com/?ArrangeActAssert)
* Custom 'Action' classes have been written for each of the commands supported by the program. This is [expected](https://docs.python.org/3/library/argparse.html#action) by `argparse`, but I dislike it.
* I sense some strong coupling between the commands and mutil modules--see the source code for details.
