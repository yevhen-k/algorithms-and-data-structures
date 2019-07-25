from __future__ import annotations

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        self._size = 0

    def prepend(self, data) -> SinglyLinkedList:
        node = Node(data)
        node.next = self.head
        self.head = node
        self._size += 1
        return self

    def append(self, data) -> SinglyLinkedList:
        node = Node(data)
        if self.head != None:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            self._size += 1
            return self
        else:
            self.head = node
            self._size += 1
            return self

    def remove_by_key(self, key) -> SinglyLinkedList:
        prev_node = self.head
        if prev_node is None:
            return self
        if prev_node.data == key:
            self.head = prev_node.next
            self._size -= 1
            return self
        cur_node = prev_node.next
        while cur_node:
            if cur_node.data == key:
                prev_node.next = cur_node.next
                cur_node.next = None
                self._size -= 1
                return self
            cur_node = cur_node.next
            prev_node = prev_node.next
        return self

    def remove_by_position(self, pos: int) -> SinglyLinkedList:
        cur_pos = 0
        prev_node = self.head
        if prev_node == None:
            return self
        if pos == 0:
            self.head = prev_node.next
            self._size -= 1
            return self
        cur_node = prev_node.next
        while cur_node:
            cur_pos += 1
            if pos == cur_pos:
                prev_node.next = cur_node.next
                cur_node.next = None
                self._size -= 1
                return self
            prev_node = prev_node.next
            cur_node = cur_node.next
        return self
        

    def insert_after(self, prev_node: Node, data) -> SinglyLinkedList:
        if prev_node is None:
            raise ValueError()
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node
        self._size += 1
        return self

    def __str__(self) -> str:
        res = '['
        if self.head is None:
            res += ']'
            return res
        node = self.head
        res += str(node.data) + ', '
        while node.next:
            node = node.next
            res += str(node.data) + ', '
        res += ']'
        res = res.replace(', ]', ']')
        return res

    def __eq__(self, value: SinglyLinkedList) -> bool:
        if type(value) != type(self):
            return False
        if len(value) != len(self):
            return False
        cur_node = self.head
        val_node = value.head
        while val_node and cur_node:
            if val_node.data != cur_node.data:
                return False
            val_node = val_node.next
            cur_node = cur_node.next
        return True

    def __len__(self) -> int:
        return self._size        
