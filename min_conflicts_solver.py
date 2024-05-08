import random

import numpy as np

from cell import Cell


def min_conflicts_solver(puzzle, max_steps: int, tabu_size: int) -> np.ndarray or None:
    """
    Min conflict algorithm, uses tabu search to not get stuck on plateaus
    :param puzzle:  Sudoku puzzle
    :param max_steps: max iterations
    :param tabu_size: number of tabu assignments stored
    :return: solution or None, if the solution was not found
    """

    # Initial complete assignment for the puzzle
    board = np.empty((9, 9), dtype=Cell)

    for i in range(9):
        for j in range(9):
            if puzzle.board[i][j] is not None:
                board[i, j] = Cell(puzzle.board[i][j])
            else:
                board[i, j] = Cell()
                board[i, j].set_value(random.randint(1, 9))  # Value is set but domain is not restricted

    tabu_list = TabuList(tabu_size)

    for step in range(max_steps):
        if is_solved(board):
            return board
        conflicting_vars = get_conflicting_variables(board)
        var = conflicting_vars[random.randint(0, len(conflicting_vars) - 1)]
        value = get_min_conflicts(board, var, tabu_list)
        board[var[0], var[1]].value = value
        tabu_list.add((var[0], var[1]), value)

    return None


def is_solved(board) -> bool:
    # Check all rows
    for i in range(9):
        values = []  # Stores all values in row
        for j in range(9):
            values.append(board[i, j].value)
            # Checking for same values
            if len(values) > len(set(values)):
                return False
    # Check all columns
    for j in range(9):
        values = []  # Stores all values in column
        for i in range(9):
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
                    values.append(board[i, j].value)
                    # Checking for same values
                    if len(values) > len(set(values)):
                        return False
    # No constraints have been broken
    return True


def get_conflicting_variables(board) -> list:
    """

    :param board: Sudoku puzzle board
    :return: List of conflicting variables tuples
    """
    conflicting_vars = []
    for i in range(9):
        for j in range(9):
            v = board[i, j].value  # Value of inspected variable
            found = False  # Found conflict
            for k in range(9):
                if not found and k != i and board[k, j].value == v:
                    found = True
                    conflicting_vars.append((i, j))
                if not found and k != j and board[i, k].value == v:
                    found = True
                    conflicting_vars.append((i, j))
            sr = i // 3
            sc = j // 3
            for m in range(sr * 3, sr * 3 + 3):
                for n in range(sc * 3, sc * 3 + 3):
                    if not found and (m, n) != (i, j) and board[m, n].value == v:
                        found = True
                        conflicting_vars.append((i, j))

    return conflicting_vars


class TabuList:
    def __init__(self, max_size):
        self.tabu = []
        self.max_size = max_size

    def add(self, var: tuple, value: int) -> None:
        while len(self.tabu) >= self.max_size:
            self.tabu.pop(0)
        self.tabu.append((var, value))

    def is_tabu(self, var, value) -> bool:
        return (var, value) in self.tabu


def get_min_conflicts(board, var: tuple, tabu_list: TabuList) -> int:
    """

    :param board: Sudoku puzzle board
    :param var: Var chosen to find minimum conflicting value in variable domain
    :param tabu_list: collection of tabu assignments
    :return: minimum conflicting value
    """

    i = var[0]
    j = var[1]

    min_conflicting_value = None
    min_conflicts = np.inf
    for v in board[i, j].domain:
        if not tabu_list.is_tabu((i, j), v):
            conflicts = 0
            for k in range(9):
                if k != j and board[i, k].value == v:  # Row conflict
                    conflicts += 1
                if k != i and board[k, j].value == v:  # Column conflict
                    conflicts += 1

            sr = i // 3  # Square row of variable
            sc = j // 3  # Square column of variable
            for m in range(sr * 3, sr * 3 + 3):
                for n in range(sc * 3, sc * 3 + 3):
                    if (m != i or n != j) and board[m, n].value == v:
                        conflicts += 1

            if conflicts < min_conflicts:
                min_conflicting_value = v
                min_conflicts = conflicts

    return min_conflicting_value
