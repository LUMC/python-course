#!/usr/bin/env python

class Stack(list):
    def push(self, element):
        self.append(element)

    def __str__(self):
        return str(self[-1])


class Calculator(Stack):
    def add(self):
        self.push(self.pop() + self.pop())

    def sub(self):
        temp = self.pop()
        self.push(self.pop() - temp)

    def mul(self):
        self.push(self.pop() * self.pop())

    def div(self):
        temp = self.pop()
        self.push(self.pop() / temp)
