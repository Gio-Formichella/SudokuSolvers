import numpy as np
from ac3 import ac3
from backtracking_search import backtracking_search


def sudoku_solver(board) -> np.ndarray or None:
    if not ac3(board):
        return None
    result = backtracking_search(board)
    return result
