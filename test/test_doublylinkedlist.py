import unittest
from data_strucures.linkedlist.doublylinkedlist import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    
    def test_equality(self):
        dl1 = DoublyLinkedList()
        dl2 = DoublyLinkedList()
        dl3 = DoublyLinkedList()
        dl4 = DoublyLinkedList()
        for i in range(5):
            dl1.prepend(i)
            dl2.prepend(i)
            dl3.append(i)
            dl4.append(i)
        self.assertEqual(dl1, dl2)
        self.assertEqual(dl3, dl4)

        dl1 = DoublyLinkedList()
        dl2 = DoublyLinkedList()
        dl3 = DoublyLinkedList()
        dl4 = DoublyLinkedList()
        for i in range(5):
            dl1.prepend(i)
            dl2.prepend(i+1)
            dl3.append(i)
            dl4.append(i+1)
        self.assertNotEqual(dl1, dl2)
        self.assertNotEqual(dl3, dl4)
        self.assertNotEqual(dl1, dl3)
        self.assertNotEqual(dl1, dl4)

        dl1 = DoublyLinkedList()
        dl2 = DoublyLinkedList()
        for i in range(5):
            if i == 2:
                dl1.prepend(i)
                continue
            dl1.prepend(i)
            dl2.prepend(i)
        self.assertNotEqual(dl1, dl2)
        dl1 = DoublyLinkedList()
        dl2 = []
        for i in range(5):
            dl1.prepend(i)
            dl2.append(i)
        self.assertNotEqual(dl1, dl2)

    def test_len(self):
        n = 10
        dl = DoublyLinkedList()
        for i in range(n):
            dl.append(i)
        self.assertEqual(n, len(dl))

        dl = DoublyLinkedList()
        for i in range(n):
            dl.prepend(i)
        self.assertEqual(n, len(dl))

        dl.insert_after(dl.head, 1)
        n += 1
        self.assertEqual(n, len(dl))

        dl.insert_before(dl.head, 1)
        self.assertEqual(n, len(dl))

        self.assertEqual(DoublyLinkedList(), 0)





if __name__ == "__main__":
    unittest.main()