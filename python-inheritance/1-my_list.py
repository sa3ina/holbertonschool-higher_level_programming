#!/usr/bin/python3
"""This module represents inheritance"""


class MyList(list):
    def print_sorted(self):
        """This class inherits list and prints"""

        print(sorted(self))
