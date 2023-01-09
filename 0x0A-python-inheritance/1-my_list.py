#!/usr/bin/python3
"""List subclass module"""


class MyList(list):
    """A derived class of the list class"""

    def __init__(self):
        """Instantiates the derived class"""
        super().__init__()

    def print_sorted(self):
        """Prints all contents of the derived class in sorted order"""
        string = self.__str__()
        lst = []
        for i in string:
            if i.isnumeric():
                lst.append(int(i))
        lst.sort()
        print((lst))
