import unittest

from backtracking_search import order_domain_values
from cell import Cell
from sudoku_solver import *

"""
To better understand the tests draw the sudoku board and add values as in setUp
"""


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        # Sudoku board
        self.b = np.empty((9, 9), dtype=Cell)

        # Initialize each element with a new Cell object
        for i in range(9):
            for j in range(9):
                self.b[i, j] = Cell()

        self.b[0, 0].set_value(1)
        self.b[0, 1].set_value(2)
        self.b[0, 2].set_value(3)
        self.b[1, 0].set_value(4)
        self.b[1, 1].set_value(5)
        self.b[1, 2].set_value(6)
        self.b[2, 0].set_value(7)
        self.b[2, 1].set_value(8)
        self.b[0, 3].set_value(4)
        self.b[0, 4].set_value(5)
        self.b[0, 5].set_value(6)
        self.b[0, 7].set_value(8)
        self.b[0, 8].set_value(9)
        self.b[3, 1].set_value(1)
        self.b[4, 1].set_value(3)
        self.b[6, 1].set_value(6)
        self.b[7, 1].set_value(7)

    def test_ac3(self):
        ac3(self.b)
        self.assertListEqual(self.b[2, 2].domain, [9])  # Square constraints
        self.assertListEqual(self.b[0, 6].domain, [7])  # Row constraints
        self.assertListEqual(self.b[5, 1].domain, [4, 9])  # Column constraints
        self.assertListEqual(self.b[3, 0].domain, [2, 5, 6, 8, 9])

    def test_order_domain_values(self):
        """
        Note: the test is also dependent on ac3. A better unit test can be achieved by removing this dependency, but I
        couldn't be bothered from going threw all the unrestricted domains of all the variables connected to tested one
        """
        ac3(self.b)
        result = order_domain_values(self.b, (3, 0))
        self.assertEqual(result[0][0], 6)  # Least constraining value
        self.assertEqual(result[0][1], 7)
        self.assertEqual(result[1][0], 9)
        self.assertEqual(result[1][1], 11)
        self.assertEqual(result[4][0], 2)  # Most constraining value
        self.assertEqual(result[4][1], 14)
        self.assertListEqual(result, [(6, 7), (9, 11), (5, 13), (8, 13), (2, 14)])
