import unittest

from sudoku import Sudoku

from min_conflicts_solver import *


class TestMinConflictSubroutines(unittest.TestCase):
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

        # Building solved board
        new_puzzle = Sudoku(3)
        solved = new_puzzle.solve()  # Using external solver that I'm sure finds a solution
        self.solved_board = np.empty((9, 9), dtype=Cell)
        for i in range(9):
            for j in range(9):
                if solved.board[i][j] is not None:
                    self.solved_board[i, j] = Cell(solved.board[i][j])
                else:
                    self.solved_board[i, j] = Cell()

    def test_is_solved(self):
        # Unsolved board
        self.assertFalse(is_solved(self.b))

        # Solved board
        self.assertTrue(is_solved(self.solved_board))

    def test_get_conflicting_variables(self):
        self.assertEqual(len(get_conflicting_variables(self.b)), 64)
        self.assertListEqual(get_conflicting_variables(self.solved_board), [])

    def test_get_min_conflicts(self):
        self.assertEqual(get_min_conflicts(self.b, (2, 2), TabuList(10)), 9)
