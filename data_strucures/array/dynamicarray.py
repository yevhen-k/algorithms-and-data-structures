from __future__ import annotations


class DynamicArray:

    # TODO
    # implement insertion to position (?)
    # implement shrink
    def __init__(self, size=10, grow_ratio=1.5):
        self._cursor = 0
        self._size = size
        self._container = [None] * self._size
        self.grow_ratio = grow_ratio

    def append(self, data) -> None:
        if self._size - 1 < self._cursor:
            new_size = int(self._size * self.grow_ratio)
            self._allocate_new_container(new_size)
        self._container[self._cursor] = data
        self._cursor += 1

    def remove_by_index(self, index: int) -> bool:
        if index < 0 or index > self._cursor:
            return False
        if index == self._cursor:
            self._container[index] = None
            self._cursor -= 1
            return True
        for i in range(index, self._cursor-1):
            self._container[i] = self._container[i+1]
        self._container[self._cursor-1] = None
        self._cursor -= 1
        return True

    def remove_by_value(self, val) -> bool:
        for i in range(self._cursor):
            if val == self.get(i):
                return self.remove_by_index(i)
        return False

    def get(self, index):
        if index < 0 or index > self._cursor:
            raise IndexError()
        return self._container[index]

    def _allocate_new_container(self, new_size: int):
        self._size = new_size
        new_container = [None] * self._size
        for i in range(len(self._container)):
            new_container[i] = self._container[i]
        self._container = new_container

    def __getitem__(self, idx):
        if idx >= self._cursor:
            raise StopIteration()
        return self._container[idx]

    def __str__(self):
        return str([self._container[i] for i in range(self._cursor)])

    def __len__(self):
        return self._cursor

    def __eq__(self, val: DynamicArray) -> bool:
        if type(self) != type(val):
            return False
        if len(self) != len(val):
            return False
        for i in range(len(val)):
            if val.get(i) != self.get(i):
                return False
        return True
