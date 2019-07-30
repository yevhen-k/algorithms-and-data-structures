from __future__ import annotations


class BinarySearchTree:

    def __init__(self, key: int, data):
        self.left = None
        self.right = None
        self.key = key
        self.data = data

    def insert_rec(self, key: int, data) -> BinarySearchTree:
        if key < self.key and self.left is not None:
            return self.left.insert_rec(key, data)
        if key < self.key and self.left is None:
            self.left = BinarySearchTree(key, data)
            return self
        if key >= self.key and self.right is not None:
            return self.right.insert_rec(key, data)
        if key >= self.key and self.right is None:
            self.right = BinarySearchTree(key, data)
            return self



    def insert(self, key: int, data) -> BinarySearchTree:
        node = BinarySearchTree(key, data)
        current_node = self
        while True:
            parent_node = current_node
            if node.key < current_node.key:
                current_node = current_node.left
                if current_node is None:
                    parent_node.left = node
                    return self
            else:
                current_node = current_node.right
                if current_node is None:
                    parent_node.right = node
                    return self

    def find(self, key: int) -> BinarySearchTree:
        current_node = self
        while current_node.key != key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node is None:
                return None
        return current_node

    def delete(self, key: int):
        pass

    def __str__(self) -> str:
        return str(self.key) + '(' + str(self.left or '_') + ', ' + str(self.right or '_') + ')'

    @staticmethod
    def pre_order(b: BinarySearchTree):
        if b is not None:
            print(b.key, ', ', end='', sep='')
            BinarySearchTree.pre_order(b.left)
            BinarySearchTree.pre_order(b.right)

    @staticmethod
    def in_order(b: BinarySearchTree):
        if b is not None:
            BinarySearchTree.in_order(b.left)
            print(b.key, ', ', end='', sep='')
            BinarySearchTree.in_order(b.right)

    @staticmethod
    def post_order(b: BinarySearchTree):
        if b is not None:
            BinarySearchTree.post_order(b.left)
            BinarySearchTree.post_order(b.right)
            print(b.key, ', ', end='', sep='')


if __name__ == '__main__':
    b = BinarySearchTree(50, 1).insert(30, 1).insert(20, 4).insert(40, 0).insert(60, 0).insert(10, 0) \
        .insert(70, 0)
    # res = b.find(-1)
    # print(b)
    # BinarySearchTree.pre_order(b)
    # print()
    # BinarySearchTree.in_order(b)
    # print()
    # BinarySearchTree.post_order(b)
    b1 = BinarySearchTree(50, 1)
    b2 = BinarySearchTree(50, 1)
    for i in [30, 20, 40, 60, 10, 70]:
        b1.insert(i, i)
        b2.insert_rec(i, i)
    print(b1)
    print(b2)
    print(str(b1) == str(b2))
