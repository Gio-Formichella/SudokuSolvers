import unittest

from backtracking_solver import *

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

    def test_revise(self):
        self.assertTrue(revise(self.b, 2, 2, 1, 2))
        self.assertFalse(revise(self.b, 1, 2, 2, 2))

    def test_ac3(self):
        self.assertTrue(ac3(self.b))
        self.assertListEqual(self.b[2, 2].domain, [9])  # Square constraints
        self.assertListEqual(self.b[0, 6].domain, [7])  # Row constraints
        self.assertListEqual(self.b[5, 1].domain, [4, 9])  # Column constraints
        self.assertListEqual(self.b[3, 0].domain, [2, 5, 6, 8, 9])

        # Invalid puzzle board
        invalid_b = np.empty((9, 9), dtype=Cell)

        # Initialize each element with a new Cell object
        for i in range(9):
            for j in range(9):
                invalid_b[i, j] = Cell()
        invalid_b[0, 0].set_value(1)
        invalid_b[1, 1].set_value(1)
        self.assertFalse(ac3(invalid_b))

    def test_order_domain_values(self):
        """
        Note: the test is also dependent on ac3. A better unit test can be achieved by removing this dependency, but I
        couldn't be bothered from going threw all the unrestricted domains of all the variables connected to tested one
        """
        ac3(self.b)
        result = order_domain_values(self.b, (3, 0))
        self.assertEqual(result[0], 6)  # Least constraining value
        self.assertEqual(result[1], 9)
        self.assertEqual(result[4], 2)  # Most constraining value
        self.assertListEqual(result, [6, 9, 5, 8, 2])

    def test_select_unassigned_variable(self):
        self.assertTupleEqual(select_unassigned_variable(self.b, "static"), (0, 6))
        # Assigning a value to all cells
        for i in range(9):
            for j in range(9):
                if self.b[i, j].value is None:
                    self.b[i, j].set_value(0)

        self.assertIsNone(select_unassigned_variable(self.b, "static"))

    def test_mac(self):
        self.b[8, 8].set_value(8)
        self.assertIsNotNone(mac(self.b, (8, 8)))
        self.assertListEqual(self.b[7, 8].domain, [1, 2, 3, 4, 5, 6, 7, 9])
        self.assertListEqual(self.b[7, 7].domain, [1, 2, 3, 4, 5, 6, 7, 9])
        self.assertListEqual(self.b[8, 7].domain, [1, 2, 3, 4, 5, 6, 7, 9])

        self.b[2, 3].domain = [9]
        self.b[2, 2].set_value(9)
        self.assertIsNone(mac(self.b, (2, 2)))

    def test_inference(self):
        self.assertIsNotNone(inference(self.b, (3, 0), 2, "mac"))
        self.b[2, 3].domain = [9]
        self.assertIsNone(inference(self.b, (2, 2), 9, "mac"))
