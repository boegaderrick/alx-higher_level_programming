#!/usr/bin/python3
"""Node class"""


class Node:
    """node object initialization"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    """returns data held in node"""
    @property
    def data(self):
        return self.__data

    """setter method for node data attribute"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    """returns next_node"""
    @property
    def next_node(self):
        return self.__next_node

    """setter function for next_node attribute"""
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):
            if value is not None:
                raise TypeError('next_node must be a Node object')
        self.__next_node = value


"""singly linked list definition"""


class SinglyLinkedList:

    """list initialization"""
    def __init__(self):
        self.__head = None

    """magic method that returns contents of linked list object as a string"""
    def __str__(self):
        temp = self.__head
        node_string = ''
        while (temp):
            s = (str(temp.data) + '\n') if temp.next_node else str(temp.data)
            node_string += s
            temp = temp.next_node
        return node_string

    """adds node in sorted order"""
    def sorted_insert(self, value):
        temp = self.__head
        new = Node(value)
        if not self.__head:
            self.__head = new
            return
        if temp.data and temp.data > value:
            new.next_node = self.__head
            self.__head = new
            return self.__head
        while temp.next_node:
            prev = temp
            temp = temp.next_node
            if temp.data > value:
                prev.next_node = new
                new.next_node = temp
                return
        temp.next_node = new
