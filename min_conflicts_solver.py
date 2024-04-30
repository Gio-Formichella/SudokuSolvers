import random

import numpy as np

from cell import Cell


def min_conflicts_solver(puzzle, max_steps: int) -> np.ndarray or None:
    # Initial complete assignment for the puzzle
    board = np.empty((9, 9), dtype=Cell)

    for i in range(9):
        for j in range(9):
            if puzzle.board[i][j] is not None:
                board[i, j] = Cell(puzzle.board[i][j])
            else:
                board[i, j] = Cell()
                board[i, j].value = random.randint(1, 9)  # Value is set but domain is not restricted

    for step in range(max_steps):
        if is_solved(board):
            conflicting_vars = get_conflicting_variables(board)
            var = conflicting_vars[random.randint(0, len(conflicting_vars) - 1)]
            value = min_conflicts(board, var)
            board[var[0], var[1]].value = value

    return None


def is_solved(board) -> bool:
    # Check all rows
    for i in range(9):
        for j in range(9):
            values = []  # Stores all values in row
            if board[i, j].value is not None:
                values.append(board[i, j].value)
            # Checking for same values
            if len(values) > len(set(values)):
                return False
    # Check all columns
    for j in range(9):
        for i in range(9):
            values = []  # Stores all values in column
            if board[i, j].value is not None:
                values.append(board[i, j].value)
            # Checking for same values
            if len(values) > len(set(values)):
                return False
    # Check all squares
    for sr in range(3):  # Square rows
        for sc in range(3):  # Square columns
            values = []  # Stores all values in square
            for i in range(sr * 3, sr * 3 + 3):
                for j in range(sc * 3, sc * 3 + 3):
                    if board[i, j].value is not None:
                        values.append(board[i, j].value)
                    # Checking for same values
                    if len(values) > len(set(values)):
                        return False
    # No constraints have been broken
    return True


def get_conflicting_variables(board) -> list:
    pass


def min_conflicts(board, var: tuple) -> int:
    pass
