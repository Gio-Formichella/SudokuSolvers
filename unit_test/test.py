import unittest
from sudoku_solver import *
import numpy as np
from cell import Cell


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        # Sudoku board
        self.b = np.empty((9, 9), dtype=Cell)

        # Initialize each element with a new Cell object
        for i in range(9):
            for j in range(9):
                self.b[i, j] = Cell()

    def test_ac3(self):
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

        ac3(self.b)
        self.assertListEqual(self.b[2, 2].domain, [9])  # Square constraints
        self.assertListEqual(self.b[0, 6].domain, [7])  # Row constraints
        self.assertListEqual(self.b[5, 1].domain, [4, 9])  # Column constraints
