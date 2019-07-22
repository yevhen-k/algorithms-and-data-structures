from sorting.squared import bubble_sort, insertion_sort, choise_sort
from sorting.linear import count_sort
from sorting.n_log_n import quicksort, _merge, mergesort, timsort
import unittest


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        A = list(range(10, -1, -1))
        B = list(A)
        bubble_sort(A)
        self.assertEqual(sorted(B), A)

        A = [0] * 10
        B = list(A)
        bubble_sort(A)
        self.assertEqual(sorted(B), A)

        A = list(range(10, 20)) + list(range(10))
        B = list(A)
        bubble_sort(A)
        self.assertEqual(sorted(B), A)

    def test_insertion_sort(self):
        A = list(range(10, -1, -1))
        B = list(A)
        insertion_sort(A)
        self.assertEqual(sorted(B), A)

        A = [0] * 10
        B = list(A)
        insertion_sort(A)
        self.assertEqual(sorted(B), A)

        A = list(range(10, 20)) + list(range(10))
        B = list(A)
        insertion_sort(A)
        self.assertEqual(sorted(B), A)

    def test_choise_sort(self):
        A = list(range(10, -1, -1))
        B = list(A)
        choise_sort(A)
        self.assertEqual(sorted(B), A)

        A = [0] * 10
        B = list(A)
        choise_sort(A)
        self.assertEqual(sorted(B), A)

        A = list(range(10, 20)) + list(range(10))
        B = list(A)
        choise_sort(A)
        self.assertEqual(sorted(B), A)

    def test_count_sort(self):
        A = list(range(10, -1, -1))
        res = count_sort(A)
        self.assertEqual(sorted(A), res)

        A = [0] * 10
        res = count_sort(A)
        self.assertEqual(sorted(A), res)

        A = list(range(10, 20)) + list(range(10))
        res = count_sort(A)
        self.assertEqual(sorted(A), res)

    def test_quicksort(self):
        A = list(range(10, -1, -1))
        res = quicksort(A)
        self.assertEqual(sorted(A), res)

        A = [0] * 10
        res = quicksort(A)
        self.assertEqual(sorted(A), res)

        A = list(range(10, 20)) + list(range(10))
        res = quicksort(A)
        self.assertEqual(sorted(A), res)

    def test_merge(self):
        A = [1,3,5,7,9]
        B = [2,4,6,8]
        res = _merge(A, B)
        self.assertEqual([1,2,3,4,5,6,7,8,9], res)
        A = [9, 10]
        B = [6, 7, 8]
        res = _merge(A, B)
        self.assertEqual([6,7,8,9,10], res)

    def test_mergesort(self):
        A = list(range(10, -1, -1))
        res = mergesort(A)
        self.assertEqual(sorted(A), res)

        A = [0] * 10
        res = mergesort(A)
        self.assertEqual(sorted(A), res)

        A = list(range(10, 20)) + list(range(10))
        res = mergesort(A)
        self.assertEqual(sorted(A), res)





if __name__ == '__main__':
    unittest.main()