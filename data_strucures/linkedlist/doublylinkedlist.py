from __future__ import annotations

class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def prepend(self, data) -> DoublyLinkedList:
        node = Node(data)
        if not self.head:
            self.head = node
            self._size +=1
            return self
        self.head.prev = node
        node.next = self.head
        self.head = node
        self._size += 1
        return self

    def append(self, data) -> DoublyLinkedList:
        node = Node(data)
        curr_node = self.head
        if curr_node:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node
            node.prev = curr_node
            self._size += 1
            return self
        else:
            self.head = node
            self._size += 1
            return self

    def insert_after(self, prev_node: Node, data) -> DoublyLinkedList:
        if not prev_node or not prev_node.next:
            return self
        node = Node(data)
        prev_node.next.prev = node
        node.next = prev_node.next
        prev_node.next = node
        node.prev = prev_node
        self._size += 1
        return self

    def insert_before(self, next_node: Node, data) -> DoublyLinkedList:
        if not next_node or not next_node.prev:
            return self
        prev_node = next_node.prev
        return self.insert_after(prev_node, data)

    def remove_by_position(self, pos: int) -> DoublyLinkedList:
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

    def remove_where(self, data) -> DoublyLinkedList:
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                if cur_node.next and cur_node.prev:
                    cur_node.prev = cur_node.next
                    self._size -= 1
                    return self
                if cur_node.next and not cur_node.prev:
                    cur_node.next.prev = None
                    self._size -= 1
                    return self
                if not cur_node.next and cur_node.prev:
                    cur_node.prev.next = None
                    self._size -= 1
                    return self
            cur_node = cur_node.next
        return self

    def __str__(self) -> str:
        res = '['
        if not self.head:
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

    def __eq__(self, val: DoublyLinkedList) -> bool:
        if type(val) != type(self):
            return False
        if len(val) != len(self):
            return False
        cur_node = self.head
        val_node = val.head
        while cur_node:
            if cur_node.data != val_node.data:
                return False
            cur_node = cur_node.next
            val_node = val_node.next
        return True

    def __len__(self) -> int:
        return self._size



if __name__ == "__main__":
    dl = DoublyLinkedList()
    dl.prepend(1).prepend(2).prepend(3).prepend(4).prepend(5)
    print(dl)
    remove = 2 # 2 3 4 5 
    print(dl.remove_where(remove), len(dl))

