import numpy as np
from queue import Queue
from backtracking_search import backtracking_search


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
                queue.push((i, j, i, k))
                queue.push((i, k, i, j))
            for m in range(i + 1, 9):
                queue.push((i, j, m, j))
                queue.push((m, j, i, j))
    # Arcs relative to square constraints
    for sr in range(3):  # Square rows
        for sc in range(3):  # Square columns
            for i in range(sr * 3, sr * 3 + 3):  # Row index within the square
                for j in range(sc * 3, sc * 3 + 3):  # Column index within the square
                    for k in range(i + 1, sr * 3 + 3):
                        for m in range(j + 1, sc * 3 + 3):
                            queue.push((i, j, k, m))
                            queue.push((k, m, i, j))
                        for n in range(sc * 3, j):
                            queue.push((i, j, k, n))
                            queue.push((k, n, i, j))

    while not queue.is_empty():
        t = queue.pop()
        i1, j1, i2, j2 = t[0], t[1], t[2], t[3]
        if revise(board, i1, j1, i2, j2):
            if len(board[i1, j1].domain) == 0:
                # Problem has no solution
                return False
            # Propagation to all neighbors
            for k in range(9):
                if k != j1 and (i1, k) != (i2, j2):
                    queue.push((i1, k, i1, j1))
                if k != i1 and (k, j1) != (i2, j2):
                    queue.push((k, j1, i1, j1))
            sr = i1 // 3
            sc = j1 // 3
            for i in range(sr*3, sr*3+3):
                for j in range(sc*3, sc*3 + 3):
                    if (i, j) not in ((i1, j1), (i2, j2)):
                        queue.push((i, j, i1, j1))

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
