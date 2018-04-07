#!/usr/bin/env python3

class Node:

    def __init__(self, data, previousNode=None, nextNode=None):
        self.data = data
        self.previousNode = previousNode
        self.nextNode =  nextNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def _non_empty_list(self):
        return self.head is not None

    def _handle_empty_list(self, data):
        if self.head == self.tail == None:
            self.head = Node(data)
            self.tail = self.head

    def add_at_end(self, data):
        self._handle_empty_list(data)
        currentNode = Node(data, self.tail)
        self.tail.nextNode = currentNode
        self.tail = currentNode

    def add_at_beginning(self, data):
        self._handle_empty_list(data)
        currentNode = Node(data, None, self.head)
        self.head.previousNode = currentNode
        self.head = currentNode

    def add_at_index(self, data, index):
        self._handle_empty_list(data)
        currentNode = self.head
        for i in range(index):
            try:
                currentNode = currentNode.nextNode
            except AttributeError:
                print('Linked list index out of range!')
                return
        newNode = Node(data, currentNode, currentNode.nextNode)
        currentNode.nextNode = newNode

    def traverse(self):
        self._traverse_helper(self.head)

    def _traverse_helper(self, currentNode):
        print(currentNode.data)
        if currentNode.nextNode is not None:
            self._traverse_helper(currentNode.nextNode)

    def remove_from_beginning(self):
        if self._non_empty_list():
            self.head = self.head.nextNode
            self.head.previousNode = None

    def remove_from_index(self, index):
        pass

    def remove_at_end(self):
        pass

class Queue(DoublyLinkedList):

    def __init__(self):
        super().__init__()
        for method in [
            'add_at_beginning', 'remove_from_index', 'remove_at_end',
            'traverse', '_traverse_helper'
        ]:
            del method





if __name__ == '__main__':
    doublyLinkedList = DoublyLinkedList()
    doublyLinkedList.add_at_end(13)
    print('{0.head.data}\n{0.tail.data}'.format(doublyLinkedList))
    doublyLinkedList.add_at_beginning(12)
    doublyLinkedList.add_at_beginning(16)
    doublyLinkedList.add_at_index(5, 3)
    doublyLinkedList.traverse()
    queue = Queue()
