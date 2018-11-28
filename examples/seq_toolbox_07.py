#!/usr/bin/env python

import sys

def calc_gc_percent(seq):
    """
    Calculates the GC percentage of the given sequence.

    Arguments:
        - seq - the input sequence (string).

    Returns:
        - GC percentage (float).

    """
    at_count, gc_count = 0, 0
    # change input to all caps to allow for non-capital
    # input sequence.
    for char in seq.upper():
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1
        else:
            raise ValueError("Unexpected character found: {}. Only "
                    "ACTGs are allowed.".format(char))

    # Corner case handling: empty input sequence.
    try:
        return gc_count * 100.0 / (gc_count + at_count)
    except ZeroDivisionError:
        return 0.0

input_seq = sys.argv[1]
print("The sequence '{}' has a %GC of {:.2f}".format(input_seq, calc_gc_percent(input_seq)))
