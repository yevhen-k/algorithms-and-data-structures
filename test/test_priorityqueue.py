import unittest
import random
from data_structures.queue.priorityqueue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def test_insert_get(self):
        length = 10
        pq = PriorityQueue()
        ll = [random.randint(0, 10) for _ in range(length)]
        sorted_ll = sorted(ll, reverse=True)
        for i in range(length):
            pq.insert(ll[i])
        for i in range(len(pq)):
            self.assertEqual(sorted_ll[i], pq.get())

    def test_getitem(self):
        length = 10
        pq = PriorityQueue()
        ll = [random.randint(0, 10) for _ in range(length)]
        sorted_ll = sorted(ll, reverse=True)
        for i in range(length):
            pq.insert(ll[i])
        for idx, val in enumerate(pq):
            self.assertEqual(sorted_ll[idx], val)


if __name__ == '__main__':
    unittest.main()
