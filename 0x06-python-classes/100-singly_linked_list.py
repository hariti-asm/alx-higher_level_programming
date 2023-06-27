#!/usr/bin/python3
"""Defines a singly linked list"""


class Node:
    """Defines a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the data"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data attribute"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets next_node attribute"""

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets next_node attribute"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the data"""

        self.head = None

    def __str__(self):
        """Prints the list"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """Inserts a node into a sorted linked list"""

        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
