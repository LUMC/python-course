#!/usr/bin/env python

import sys

def calc_gc_percent(seq):
    at_count, gc_count = 0, 0
    for char in seq.upper():
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1

    return gc_count * 100.0 / (gc_count + at_count)

input_seq = sys.argv[1]
print "The sequence '{}' has a %GC of {:.2f}".format(input_seq, calc_gc_percent(input_seq))
