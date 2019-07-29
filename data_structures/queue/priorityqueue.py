from __future__ import annotations
from data_structures.array.dynamicarray import DynamicArray
from data_structures.queue.deque import Deque


class StrictPriorityQueue:

    def __init__(self, priorities: int):
        """
        :param priorities: is the number of priorities that
        can be processed. If *priorities* is given as 5 there are
        5 available types of priorities: 1, 2, 3, 4, 5.
        Numbers such as N <= 0 are not allowed to be an initializers for
        *priorities* property
        """
        self._priorities = priorities
        self._p_array = DynamicArray(self._priorities)
        for priority in range(self._priorities):
            self._p_array.append(Deque())
        self._num_of_elem = 0

    def insert(self, priority: int, data) -> StrictPriorityQueue:
        if priority > self._priorities or priority <= 0:
            raise IndexError('Not allowed priority for the given StrictPriorityQueue')
        self._p_array.get(priority-1).push_last(data)
        self._num_of_elem += 1
        return self

    def get(self):
        if self.is_empty():
            raise Exception('StrictPriorityQueue is already exhausted')
        for priority in range(self._priorities, 0, -1):
            if self._p_array.get(priority-1).is_empty():
                continue
            self._num_of_elem -= 1
            return self._p_array.get(priority-1).pop_first()

    def is_empty(self):
        return self._num_of_elem == 0

    def has_more(self):
        return self._num_of_elem > 0

    def __str__(self) -> str:
        res = list()
        res.append('[\n')
        for priority in range(self._priorities, 0, -1):
            res.append('\t' + str(priority) + ': ' + str(self._p_array.get(priority-1)) + '\n')
        res.append(']')
        return ''.join(res)
