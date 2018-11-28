#!/usr/bin/env python

def calc_gc_percent(seq):
    at_count, gc_count = 0, 0
    for char in seq:
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1

    return gc_count * 100.0 / (gc_count + at_count)

print("The sequence 'CAGG' has a %GC of {:.2f}".format(calc_gc_percent("CAGG")))
