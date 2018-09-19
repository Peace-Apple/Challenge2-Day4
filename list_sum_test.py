import unittest

from list_sum import sum

class Testsum(unittest.TestCase):

    def test_sum_with_negative_items(self):
        self.assertEqual(sum([-1, -2, [4, 6]]), 7)

    def test_sum(self):

        self.assertEqual(sum([1, 2, [3, 5]]), 11)

    def test_input_is_not_list(self):
        self.assertEqual(sum((4, 2, 3)),
                         'Invalid argument. It should be a list')


if __name__ == '__main__':
    unittest.main()