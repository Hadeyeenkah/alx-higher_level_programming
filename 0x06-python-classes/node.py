#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node


# Example usage:
if __name__ == "__main__":
    # Creating nodes
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(15)

    # Creating a singly linked list and adding nodes
    linked_list = SinglyLinkedList()
    linked_list.head = node1
    node1.next_node = node2
    node2.next_node = node3

    # Printing the linked list
    print(linked_list)

    # Inserting a new node in sorted order
    linked_list.sorted_insert(12)

    # Printing the updated linked list
    print(linked_list)
