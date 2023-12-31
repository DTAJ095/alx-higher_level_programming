#!/usr/bin/python3

"""Define a class Node"""


class Node:
    """Define attirbutes

    Attirbutes:
        data: the data the node will hold
        next_node: the address of the next node
    """

    def __init__(self, data, next_node=None):
        """Initialize a new node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the data private attribute value"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int) or type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets and stes the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list.

        Attributes:
            head: the head of the list
    """

    def __init__(self):
        """Initialize a list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node in a list
            The node is inserted in an ordered numerical position

            Args:
                value(Node): the node to insert
        """
        new_nd = Node(value)
        if self.__head is None:
            new_nd.next_node = None
            self.__head = new_nd
        elif self.__head.data > value:
            new_nd.next_node = self.__head
            self.__head = new_nd
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_nd.next_node = tmp.next_node
            tmp.next_node = new_nd

    def __str__(self):
        """define the representation of the list"""
        lists = []
        tmp = self.__head
        while tmp is not None:
            lists.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(lists))
