#!/usr/bin/env python
"""
Skeleton command line program.

This skeleton program does not do anything useful. It does this by not having
any real functionality implemented. This missing functionality is intentional
and should therefore not be reported as a bug.

The input should be in no particular format and the output is a magic number
written to standard output.


Run with no arguments for usage info. You'll see that the top part (up to the
double empty line) of this docstring is printed if you pass the -h argument.

Todo: Implement some functionality.
Todo: Send this to my code review partner for review.

Note: If you publish this program, please mention the license under which you
    make it available here, together with a reference to the full license
    text.

2013 Your Name <your.email@address>
"""


import argparse


def skeleton(input, magic_number):
    """
    The real main function of this program. We intentionally use a separate
    function other than `main()` to make it easy to use this stand alone
    program as a module.

    :arg input: Open readable handle to the input file.
    :type input: file
    :arg magic_number: Number to use in none of the calculations.
    :type magic_number: int

    The `magic_number` argument is written to standard output.
    """
    if not input.readline():
        # Not the input we were looking for
        raise EOFError('The input file seems to be empty.')

    print magic_number


def main():
    """
    Main entry point.

    Note that the input file can be specified as ``-`` in which case standard
    input is used. Passing the ``-h`` argument causes a help text to be
    printed.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__.split('\n\n\n')[0],
        epilog='You can add some extra information about the arguments here.')
    parser.add_argument('input', metavar='INPUT_FILE',
        type=argparse.FileType('r'), help='file used as input')
    parser.add_argument('-m', '--magic-number', dest='magic_number', type=int,
        default=42, help='your choice (%(type)s default: %(default)s)')
    args = parser.parse_args()

    try:
        skeleton(args.input, args.magic_number)
    except EOFError as error:
        parser.error(error)


if __name__ == '__main__':
    main()
