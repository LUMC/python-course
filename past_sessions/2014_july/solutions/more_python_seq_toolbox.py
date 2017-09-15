#!/usr/bin/env python

"""
My sequence toolbox module.
"""

import argparse


def calc_gc_percent(seq):
    """Calculates the GC percentage of the given sequence.

    Arguments:
        - seq - the input sequence (string).

    Returns:
        - GC percentage (float).

    The returned value is always <= 100.0

    """
    at_count, gc_count = 0, 0
    # change input to all caps to allow for non-capital input sequence
    for char in seq.upper():
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1
        else:
            raise ValueError("Invalid character found: {}".format(char))
    # corner case handling: empty input sequence
    try:
        return (gc_count * 100.0) / (at_count + gc_count)
    except ZeroDivisionError:
        return 0.0


def _show_results(seq, seq_gc):
    """Prints the sequence and its GC content.

    Arguments:
        - seq - sequence to print (string).
        - seq_gc - GC percentage (float).

    Returns:
        - None

    """
    print "The sequence '{}' has a %GC of {:.2f}".format(seq, seq_gc)


if __name__ == '__main__':

    # create our argument parser object
    parser = argparse.ArgumentParser()
    # add argument for input type
    parser.add_argument('mode', type=str,
            choices=['file', 'text'],
            help="Input type of the script")
    # add argument for the input value
    parser.add_argument('value', type=str,
            help="Input value of the script")
    # do the actual parsing
    args = parser.parse_args()

    if args.mode == 'file':
        try:
            f = open(args.value, 'r')
            for line in f:
                seq = line.strip()
                gc = calc_gc_percent(seq)
                _show_results(seq, gc)
        finally:
            f.close()
    else:
        _show_results(args.value, calc_gc_percent(args.value))
