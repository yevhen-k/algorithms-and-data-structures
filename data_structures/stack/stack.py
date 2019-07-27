from __future__ import annotations
from data_structures.array.dynamicarray import DynamicArray


class Stack(DynamicArray):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def push(self, data) -> Stack:
        self.append(data)
        return self

    def pop(self):
        last = len(self) - 1
        data = self.get(last)
        self.remove_by_index(last)
        return data

    def has_more(self) -> bool:
        return self._cursor > 0

