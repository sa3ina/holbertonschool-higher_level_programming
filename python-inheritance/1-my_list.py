#!/usr/bin/python3
"""This module represents inheritance"""


class MyList(list):
    """This class inherits from list"""

    def print_sorted(self):
        """This function prints list"""

        print(sorted(self))
