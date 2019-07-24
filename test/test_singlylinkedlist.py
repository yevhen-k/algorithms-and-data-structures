import unittest
from data_strucures.linkedlist.singlylinkedlist import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def test_equality(self):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()
        ll3 = SinglyLinkedList()
        fake_ll = []
        for i in range(5):
            ll1.append(i)
            ll2.append(i + 1)
            fake_ll.append(i)
        ll3.append(0)
        ll3.append(1)
        self.assertEqual(ll1, ll1)
        self.assertNotEqual(ll1, ll2)
        self.assertNotEqual(ll1, ll3)
        self.assertNotEqual(ll1, fake_ll)

    def generate_date_to_test_remove(self, remove_idx, length):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()
        removed_key = 0
        for i in range(length):
            if i == remove_idx:
                ll1.append(i)
                removed_key = i
                continue
            ll1.append(i)
            ll2.append(i)
        return ll1, ll2, removed_key

    def test_remove_by_key(self):
        ll1, ll2, removed_key = self.generate_date_to_test_remove(0, 5)
        self.assertEqual(ll1.remove_by_key(removed_key), ll2)
        ll1, ll2, removed_key = self.generate_date_to_test_remove(2, 5)
        self.assertEqual(ll1.remove_by_key(removed_key), ll2)
        ll1, ll2, removed_key = self.generate_date_to_test_remove(4, 5)
        self.assertEqual(ll1.remove_by_key(removed_key), ll2)

    def test_remove_by_position(self):
        ll1, ll2, removed_pos = self.generate_date_to_test_remove(0, 5)
        self.assertEqual(ll1.remove_by_position(removed_pos), ll2)
        ll1, ll2, removed_pos = self.generate_date_to_test_remove(2, 5)
        self.assertEqual(ll1.remove_by_position(removed_pos), ll2)
        ll1, ll2, removed_pos = self.generate_date_to_test_remove(4, 5)
        self.assertEqual(ll1.remove_by_position(removed_pos), ll2)

    def test_len(self):
        length = 10
        ll1, _, _ = self.generate_date_to_test_remove(0, length)
        for _ in range(length):
            length -= 1
            ll1.remove_by_position(length)
            self.assertEqual(length, len(ll1))

        length = 10
        ll1, _, _ = self.generate_date_to_test_remove(0, length)
        for _ in range(length):
            length -= 1
            ll1.remove_by_key(length)
            self.assertEqual(length, len(ll1))
        
        ll1 = SinglyLinkedList()
        for i in range(1, 11):
            ll1.append(i)
            self.assertEqual(i, len(ll1))
        
        ll1 = SinglyLinkedList()
        for i in range(1, 11):
            ll1.prepend(i)
            self.assertEqual(i, len(ll1))



if __name__ == "__main__":
    unittest.main()