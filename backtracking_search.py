import copy
import random
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


def select_unassigned_variable(csp, strategy="static") -> tuple or None:
    unassigned_var = []
    for i in range(9):
        for j in range(9):
            if csp[i, j].value is None:
                unassigned_var.append((i, j))

    match strategy:
        case "static":  # Choosing first variable in static ordering
            return unassigned_var[0]
        case "random":  # Randomly selecting unassigned variable
            idx = random.randint(0, len(unassigned_var))
            return unassigned_var[idx]
        # can add more


def order_domain_values(board: np.ndarray[Cell], var: tuple) -> list:
    i = var[0]
    j = var[1]
    least_constraining_value = []  # Will store for every value in variable domain (value, constraint_score)
    neighbors = []  # Stores neighbouring variables
    # Adding neighbors
    for k in range(9):
        if k != j:
            neighbors.append((i, k))
        if k != i:
            neighbors.append((k, j))
    sr = i // 3  # Square row of variable
    sc = j // 3  # Square column of variable
    for m in range(sr * 3, sr * 3 + 3):
        for n in range(sc * 3, sc * 3 + 3):
            if (m, n) != (i, j):
                neighbors.append((m, n))

    for value in board[i, j].domain:
        count = 0  # Times value is present in neighbors' domain
        for n in neighbors:
            if value in board[n[0], n[1]].domain:
                count += 1
        least_constraining_value.append((value, count))

    least_constraining_value.sort(key=lambda x: x[1])
    return least_constraining_value


def inference(board, var, value) -> np.ndarray or None:
    i = var[0]
    j = var[1]
    board[i, j].set_value(value)
    inference_board = mac(board, (i, j))
    return inference_board


def mac(board, var) -> np.ndarray or None:
    pass
