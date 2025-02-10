#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterador):
        self.iterator = iter(iterador)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        iter = next(self.iterator)
        self.counter += 1
        return iter
