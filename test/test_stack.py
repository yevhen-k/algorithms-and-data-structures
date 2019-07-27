import unittest
from data_structures.stack.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        length = 100
        s = Stack()
        lst = []
        for i in range(length):
            s.push(i)
            lst.append(i)
        self.assertEqual(len(s), length)
        self.assertEqual(str(lst), str(s))

    def test_pop(self):
        length = 100
        s = Stack()
        lst = []
        for i in range(length):
            s.push(i)
            lst.append(i)
        while s.has_more():
            s_item = s.pop()
            lst_item = lst.pop()
            self.assertEqual(s_item, lst_item)
            self.assertEqual(len(s), len(lst))


if __name__ == '__main__':
    unittest.main()
