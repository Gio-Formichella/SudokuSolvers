import unittest
from min_conflicts_solver import *
from sudoku import Sudoku

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

    def test_is_solved(self):
        # Unsolved board
        self.assertFalse(is_solved(self.b))

        # Building solved board
        new_puzzle = Sudoku(3)
        solved = new_puzzle.solve()  # Using external solver that I'm sure finds a solution
        board = np.empty((9, 9), dtype=Cell)
        for i in range(9):
            for j in range(9):
                if solved.board[i][j] is not None:
                    board[i, j] = Cell(solved.board[i][j])
                else:
                    board[i, j] = Cell()

        self.assertTrue(is_solved(board))
