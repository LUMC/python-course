#!/usr/bin/env python

import random

class Sequence(object):
    bases = ['A', 'C', 'G', 'T']

    def __init__(self, spots, readlength=100):
        self.cycle = 0
        self.readlength = readlength
        self.spots = spots

    def __iter__(self):
        return self

    def __len__(self):
        return self.readlength

    def next(self):
        self.cycle += 1
        if self.cycle > self.readlength:
            raise StopIteration

        tile = []
        for _ in range(self.spots):
            nucleotide = self.bases[random.randrange(4)]
            quality = 40 - (self.cycle * random.randrange(40) /
                self.readlength)
            tile.append((nucleotide, quality))

        return tile

class Read(object):
    def __init__(self):
        self.read = []
        self.qual = []

    def __str__(self):
        return "".join(self.read)

    def append(self, base):
        self.read.append(base[0])
        self.qual.append(base[1])

    def quality(self):
        return sum(self.qual) / len(self.read)

    def trim(self, score):
        for position in range(len(self.read) - 1, -1, -1):
            if self.qual[position] >= score:
                self.read = self.read[:position + 1]
                self.qual = self.qual[:position + 1]
                break

def with_class():
    spots = 2
    run = Sequence(spots)

    reads = [Read() for _ in range(spots)]
    for tile in run:
        for read_id, base in enumerate(tile):
            reads[read_id].append(base)

    for i in reads:
        print i, i.quality()
        i.trim(39)
        print i, i.quality()

def quality(quals):
    return sum(quals) / len(quals)

def trim(read, quals, score):
    for position in range(len(read) - 1, 0, -1):
        if quals[position] >= score:
            return read[:position + 1], quals[:position + 1]

def without_class():
    spots = 2
    run = Sequence(spots)

    reads = ["" for _ in range(spots)]
    quals = [[] for _ in range(spots)]
    for tile in run:
        for read_id, base in enumerate(tile):
            reads[read_id] += base[0]
            quals[read_id].append(base[1])

    for read_id, read in enumerate(reads):
        print read, quality(quals[read_id])
        read, quals[read_id] = trim(read, quals[read_id], 39)
        print read, quality(quals[read_id])

if __name__ == "__main__":
    #without_class()
    with_class()
