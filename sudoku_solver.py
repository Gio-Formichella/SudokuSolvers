import numpy as np
from backtracking_search import backtracking_search
from queue import Queue
from cell import Cell
import random


def sudoku_solver(board) -> np.ndarray or None:
    if not ac3(board):
        return None
    result = backtracking_search(board)
    return result


def ac3(board) -> bool:
    queue = Queue()
    # Arcs relative to row and column constraints
    for i in range(9):
        for j in range(9):
            for k in range(j + 1, 9):
                # First two indices are the position of the first variable in the matrix while the last two are for
                # the second variable
                queue.put((i, j, i, k))
                queue.put((i, k, i, j))
            for m in range(i + 1, 9):
                queue.put((i, j, m, j))
                queue.put((m, j, i, j))
    # Arcs relative to square constraints
    for sr in range(3):  # Square rows
        for sc in range(3):  # Square columns
            for i in range(sr * 3, sr * 3 + 3):  # Row index within the square
                for j in range(sc * 3, sc * 3 + 3):  # Column index within the square
                    for k in range(i + 1, sr * 3 + 3):
                        for m in range(j + 1, sc * 3 + 3):
                            queue.put((i, j, k, m))
                            queue.put((k, m, i, j))
                        for n in range(sc * 3, j):
                            queue.put((i, j, k, n))
                            queue.put((k, n, i, j))

    while not queue.empty():
        t = queue.get()
        i1, j1, i2, j2 = t[0], t[1], t[2], t[3]
        if revise(board, i1, j1, i2, j2):
            if len(board[i1, j1].domain) == 0:
                # Problem has no solution
                return False
            # Propagation to all neighbors
            for k in range(9):
                if k != j1 and (i1, k) != (i2, j2):
                    queue.put((i1, k, i1, j1))
                if k != i1 and (k, j1) != (i2, j2):
                    queue.put((k, j1, i1, j1))
            sr = i1 // 3
            sc = j1 // 3
            for i in range(sr * 3, sr * 3 + 3):
                for j in range(sc * 3, sc * 3 + 3):
                    if (i, j) not in ((i1, j1), (i2, j2)):
                        queue.put((i, j, i1, j1))

    return True


def revise(board, i1: int, j1: int, i2: int, j2: int) -> bool:
    revised = False
    for x in board[i1, j1].domain:
        found = False  # x admissibility
        for y in board[i2, j2].domain:
            if y != x:
                found = True

        if not found:
            board[i1, j1].domain.remove(x)
            revised = True

    return revised


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
            if m != i and n != j:
                neighbors.append((m, n))

    for value in board[i, j].domain:
        count = 0  # Times value is present in neighbors' domain
        for n in neighbors:
            if value in board[n[0], n[1]].domain:
                count += 1
        least_constraining_value.append((value, count))

    least_constraining_value.sort(key=lambda x: x[1])
    return least_constraining_value
