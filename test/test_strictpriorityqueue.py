import unittest
from data_structures.queue.priorityqueue import StrictPriorityQueue


class TestStrictPriorityQueue(unittest.TestCase):

    def test_insert_get(self):
        length = 5
        start, mid, end = 1, 3, 5
        spq = StrictPriorityQueue(length)
        for i in range(5):
            spq.insert(start, 10 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(mid, 10 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(end, 10 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(end, 50 + i)
            spq.insert(start, 10 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(start, 10 + i)
            spq.insert(end, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(start, 10 + i)
            spq.insert(mid, 30 + i)
            spq.insert(end, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 30 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(start, 10 + i)
            spq.insert(end, 50 + i)
            spq.insert(mid, 30 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 30 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(mid, 30 + i)
            spq.insert(start, 10 + i)
            spq.insert(end, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 30 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

        for i in range(5):
            spq.insert(end, 50 + i)
            spq.insert(mid, 30 + i)
            spq.insert(start, 10 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 50 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 30 + i)
        for i in range(5):
            data = spq.get()
            self.assertEqual(data, 10 + i)

    def test_has_more(self):
        length = 5
        start, mid, end = 1, 3, 5
        spq = StrictPriorityQueue(length)

        self.assertEqual(False, spq.has_more())
        for i in range(5):
            spq.insert(start, 10 + i)
            spq.insert(end, 10 + i)
            spq.insert(mid,  10 + i)
        for _ in range(3*length):
            self.assertEqual(True, spq.has_more())
            spq.get()
        self.assertEqual(False, spq.has_more())

        for i in range(5):
            spq.insert(start, 10 + i)
            spq.insert(end, 10 + i)
            spq.insert(mid,  10 + i)
        while spq.has_more():
            self.assertEqual(True, spq.has_more())
            spq.get()
        self.assertEqual(False, spq.has_more())

    def test_is_empty(self):
        length = 5
        start, mid, end = 1, 3, 5
        spq = StrictPriorityQueue(length)

        self.assertEqual(True, spq.is_empty())
        for i in range(5):
            spq.insert(start, 10 + i)
            spq.insert(end, 10 + i)
            spq.insert(mid, 10 + i)
        for _ in range(3 * length):
            self.assertEqual(False, spq.is_empty())
            spq.get()
        self.assertEqual(True, spq.is_empty())

        for i in range(5):
            spq.insert(start, 10 + i)
            spq.insert(end, 10 + i)
            spq.insert(mid, 10 + i)
        while not spq.is_empty():
            self.assertEqual(False, spq.is_empty())
            spq.get()
        self.assertEqual(True, spq.is_empty())


if __name__ == '__main__':
    unittest.main()
