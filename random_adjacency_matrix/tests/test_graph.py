import unittest
from graph import _calc_fill_pos


class GenGraphTest(unittest.TestCase):
    def test_fill_pos(self):
        self.assertEqual(_calc_fill_pos(2, 0), (0, 1))
        self.assertEqual(_calc_fill_pos(4, 4), (1, 3))
        self.assertEqual(_calc_fill_pos(5, 6), (0, 4))
