#!/usr/bin/python3
"""inherited class MyList"""


class MyList(list):
    """inherited class"""
    def print_sorted(self):
        """"Comments"""
        print(sorted(self))
