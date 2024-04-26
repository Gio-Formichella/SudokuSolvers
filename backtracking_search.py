import copy
import random
from queue import Queue

import numpy as np

from cell import Cell


def backtracking_search(board) -> np.ndarray or None:
    return backtrack(board)


def backtrack(board) -> np.ndarray or None:
    # Checking for complete assignment
    found = False
    for i in range(9):
        for j in range(9):
            if board[i, j].value is None:
                found = True
    if not found:
        return board

    var = select_unassigned_variable(board)  # tuple (row, column)
    for value in order_domain_values(board, var):
        inference_board = inference(copy.deepcopy(board), var, value)
        if inference_board is not None:
            result = backtrack(inference_board)
            if result is not None:
                return result

    return None


def inference(board, var, value) -> np.ndarray or None:
    i = var[0]
    j = var[1]
    board[i, j].set_value(value)
    if mac(board, (i, j)):
        return board
    else:
        return None
