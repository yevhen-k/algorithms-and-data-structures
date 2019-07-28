import unittest
from data_structures.queue.deque import Deque


class TestDeque(unittest.TestCase):
    def test_has_more(self):
        capacity = 10
        q = Deque(capacity=capacity)
        self.assertEqual(False, q.has_more())
        for i in range(capacity):
            q.push_front(i)
            self.assertEqual(True, q.has_more())
        for i in range(capacity):
            self.assertEqual(True, q.has_more())
            q.pop_first()
        self.assertEqual(False, q.has_more())

        q = Deque(capacity=capacity)
        self.assertEqual(False, q.has_more())
        for i in range(capacity):
            q.push_front(i)
            self.assertEqual(True, q.has_more())
        for i in range(capacity):
            self.assertEqual(True, q.has_more())
            q.pop_last()
        self.assertEqual(False, q.has_more())

        q = Deque(capacity=capacity)
        self.assertEqual(False, q.has_more())
        for i in range(capacity):
            q.push_last(i)
            self.assertEqual(True, q.has_more())
        for i in range(capacity):
            self.assertEqual(True, q.has_more())
            q.pop_first()
        self.assertEqual(False, q.has_more())

        q = Deque(capacity=capacity)
        self.assertEqual(False, q.has_more())
        for i in range(capacity):
            q.push_last(i)
            self.assertEqual(True, q.has_more())
        for i in range(capacity):
            self.assertEqual(True, q.has_more())
            q.pop_last()
        self.assertEqual(False, q.has_more())

    def test_push_front_pop_first(self):
        capacity = 10
        q = Deque(capacity=capacity)
        for i in range(capacity):
            q.push_front(i)
        for i in range(capacity-1, -1, -1):
            self.assertEqual(i, q.pop_first())

    def test_push_front_pop_last(self):
        capacity = 10
        q = Deque(capacity=capacity)
        for i in range(capacity):
            q.push_front(i)
        for i in range(capacity):
            self.assertEqual(i, q.pop_last())

    def test_push_last_pop_first(self):
        capacity = 10
        q = Deque(capacity=capacity)
        for i in range(capacity):
            q.push_last(i)
        for i in range(capacity):
            self.assertEqual(i, q.pop_first())

    def test_push_last_pop_last(self):
        capacity = 10
        q = Deque(capacity=capacity)
        for i in range(capacity):
            q.push_last(i)
        for i in range(capacity-1, -1, -1):
            self.assertEqual(i, q.pop_last())

    def test_peek_(self):
        capacity = 10
        q = Deque(capacity=capacity)
        q.push_front(0).push_front(1)
        self.assertEqual(1, q.peek_first())
        self.assertEqual(0, q.peek_last())
        self.assertEqual(2, len(q))

    def test_exception(self):
        q = Deque(capacity=1)
        q.push_front(1)
        self.assertRaises(Exception, q.push_front, (1, ))
        self.assertRaises(Exception, q.push_last, (1,))
        q.pop_last()
        self.assertRaises(Exception, q.pop_last)
        self.assertRaises(Exception, q.pop_first)


if __name__ == '__main__':
    unittest.main()
