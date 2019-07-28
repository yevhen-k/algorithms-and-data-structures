from __future__ import annotations
from data_structures.linkedlist.doublylinkedlist import DoublyLinkedList


class Deque(DoublyLinkedList):

    def __init__(self, capacity=None):
        super().__init__()
        self._capacity = capacity

    def push_front(self, data) -> Deque:
        if not self.is_full():
            return self.prepend(data)
        else:
            raise Exception('Deque is already full!')

    def push_last(self, data) -> Deque:
        if not self.is_full():
            return self.append(data)
        else:
            raise Exception('Deque is already full!')

    def pop_first(self):
        if self.has_more():
            if len(self) > 1:
                next_node = self.head.next
                data = self.head.data
                self.head = next_node
                next_node.prev = None
                self._size -= 1
                return data
            else:
                data = self.head.data
                self.tail = None
                self.head = None
                self._size -= 1
                return data
        else:
            raise Exception('Deque is empty!')

    def pop_last(self):
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
            raise Exception('Deque is empty!')

    def peek_first(self):
        if not self.is_empty():
            return self.head.data
        else:
            raise Exception('Deque is empty!')

    def peek_last(self):
        if not self.is_empty():
            return self.tail.data
        else:
            raise Exception('Deque is empty!')

    def has_more(self) -> bool:
        return len(self) > 0

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_full(self) -> bool:
        if self._capacity:
            return len(self) == self._capacity
        return False
