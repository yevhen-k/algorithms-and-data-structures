import unittest
from data_structures.queue.queue import Queue


class TestQueue(unittest.TestCase):

    def test_has_more(self):
        capacity = 10
        q = Queue(capacity=capacity)
        self.assertEqual(False, q.has_more())
        for i in range(capacity):
            q.enqueue(i)
            self.assertEqual(True, q.has_more())
        for i in range(capacity):
            self.assertEqual(True, q.has_more())
            q.dequeue()
        self.assertEqual(False, q.has_more())

    def test_queue_dequeue(self):
        capacity = 10
        q = Queue(capacity=capacity)
        for i in range(capacity):
            q.enqueue(i)
        for i in range(capacity):
            self.assertEqual(i, q.dequeue())

    def test_exception(self):
        q = Queue(capacity=1)
        q.enqueue(1)
        self.assertRaises(Exception, q.enqueue, (1, ))
        q.dequeue()
        self.assertRaises(Exception, q.dequeue)


if __name__ == '__main__':
    unittest.main()
