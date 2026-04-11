#!/usr/bin/python3
"""rnsiu"""


class CountedIterator:
    """ydshi"""
    def __init__(self, iterator, counter):
        self.iterator = iter(iterator)
        self.counter = 0
    def __next__(self):
        a = next(self.iterator)
        self.counter += 1
        
    def get_count(self):
        return self.counter