#!/usr/bin/python3
"""List subclass module"""


class MyList(list):
    """A derived class of the list class"""

    def __init__(self):
        """Instantiates the derived class"""
        super().__init__()

    def print_sorted(self):
        """Prints all contents of the derived class in sorted order"""
        st = self.__str__()
        lst = []
        for i in range(len(st)):
            if st[i].isnumeric():
                if st[i - 1] == '-':
                    lst.append(int(st[i]) * -1)
                else:
                    lst.append(int(st[i]))
        lst.sort()
        for i in lst:
            print(i)
        print('\n')
        #print((lst))
