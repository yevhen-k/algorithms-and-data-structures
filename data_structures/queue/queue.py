from __future__ import annotations
from data_structures.linkedlist.doublylinkedlist import DoublyLinkedList


class Queue(DoublyLinkedList):

    def __init__(self, capacity=None):
        """
        :param capacity: defines capacity of Queue,
        if None then capacity is unlimited
        """
        super().__init__()
        self._capacity = capacity

    def enqueue(self, data) -> Queue:
        if not self.is_full():
            return self.prepend(data)
        else:
            raise Exception('Queue is already full!')

    def dequeue(self):
        if self.has_more():
            if len(self) > 1:
                prev_node = self.tail.prev
                data = self.tail.data
                self.tail = prev_node
                prev_node.next = None
                self._size -= 1
                return data
            else:
                node = self.tail
                data = node.data
                self.tail = None
                self.head = None
                self._size -= 1
                return data
        else:
            raise Exception('Queue is empty!')

    def has_more(self) -> bool:
        return len(self) > 0

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_full(self) -> bool:
        if self._capacity:
            return len(self) == self._capacity
        return False
