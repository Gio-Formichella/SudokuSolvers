import numpy as np

from cell import Cell


def satisfied_constraints(board) -> bool:
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


b = np.full((9, 9), Cell())
print(satisfied_constraints(b))
