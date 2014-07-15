#!/usr/bin/env python

import math

from calculator import Calculator

class ScientificCalculator(Calculator):
    def pow(self):
        temp = self.pop()
        self.push(self.pop() ** temp)

    def sqrt(self):
        self.push(math.sqrt(self.pop()))


s = ScientificCalculator()
s.push(2)
s.push(3)
s.pow()
print s
s.sqrt()
print s
