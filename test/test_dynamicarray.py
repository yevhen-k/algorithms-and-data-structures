import unittest
from data_structures.array.dynamicarray import DynamicArray


class TestDynamicArray(unittest.TestCase):

    @staticmethod
    def generate_data(length: int, remove_idx):
        da1 = DynamicArray()
        da2 = DynamicArray()
        removed_val = None
        for i in range(length):
            if i == remove_idx:
                da1.append(i)
                removed_val = i
                continue
            da1.append(i)
            da2.append(i)
        return da1, da2, removed_val

    def test_remove_by_value(self):
        length = 10
        remove_idx = 0
        da1, da2, removed_val = self.generate_data(length, remove_idx)
        da1.remove_by_value(removed_val)
        self.assertEqual(da1, da2)

        remove_idx = 5
        da1, da2, removed_val = self.generate_data(length, remove_idx)
        da1.remove_by_value(removed_val)
        self.assertEqual(da1, da2)

        remove_idx = 9
        da1, da2, removed_val = self.generate_data(length, remove_idx)
        da1.remove_by_value(removed_val)
        self.assertEqual(da1, da2)

    def test_remove_by_index(self):
        length = 10
        remove_val = 0
        da1, da2, removed_idx = self.generate_data(length, remove_val)
        da1.remove_by_index(removed_idx)
        self.assertEqual(da1, da2)

        remove_val = 5
        da1, da2, removed_idx = self.generate_data(length, remove_val)
        da1.remove_by_index(removed_idx)
        self.assertEqual(da1, da2)

        remove_val = 9
        da1, da2, removed_idx = self.generate_data(length, remove_val)
        da1.remove_by_index(removed_idx)
        self.assertEqual(da1, da2)

    def test_len(self):
        da = DynamicArray()
        da1 = DynamicArray()
        length = 100
        for i in range(length):
            da.append(i)
            da1.append(i)
            self.assertEqual(i+1, len(da))
        for i in range(length-1, -1, -1):
            da.remove_by_value(i)
            self.assertEqual(i, len(da))
        for i in range(length):
            da1.remove_by_value(i)
            self.assertEqual(length-(i+1), len(da1))


if __name__ == '__main__':
    unittest.main()
