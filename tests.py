import random
import string
import unittest
from heap_sort import heap_sort


class HeapSortTests(unittest.TestCase):

    def test_empty_string_arr(self):
        arr = ['']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_empty_arr(self):
        arr = []
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_string_arr(self):
        arr = ['hello', 'i sort it', 'python', 'algorithms', 'urfu']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_string_russian_arr(self):
        arr = ['сортировка', 'питон', 'строка', 'не число']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_different_case_string(self):
        arr = ['HELLO', 'hello', 'PYthon', 'python', 'algorithms', 'URFU', 'DATA']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_int_arr(self):
        arr = [1, 5, 0, 10, 45, 5, 12]
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_big_int_arr(self):
        arr = []
        for i in range(100000):
            arr.append(random.randint(0, 50))
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_big_string_arr(self):
        arr = []
        for i in range(100000):
            arr.append(random.choice(string.ascii_letters))
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_equals_string(self):
        arr = ['q', 'q', 'q']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)

    def test_equals_int(self):
        arr = [25, 25, 25]
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(heap_sort(arr), arr2)


if __name__ == "__main__":
    unittest.main()
