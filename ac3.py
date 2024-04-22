def ac3(board) -> bool:
    queue = Queue()
    # Arcs relative to row and column constraints
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                # First two indices are the position of the first variable in the matrix while the last two are for
                # the second variable
                queue.push((i, j, i, k))
                queue.push((i, k, i, j))
    # Add arcs relative to squares
    for sr in range(3):  # Square rows
        for sc in range(3):  # Square columns
            for i in range(sr*3, sr*3+3):  # Row index within the square
                for j in range(sc*3, sc*3+3):  # Column index within the square
                    for k in range(i, sr*3+3):
                        for l in range(j+1, sc*3+3):
                            queue.push((i, j, k, l))
                            queue.push((k, l, i, j))

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
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def pop(self) -> tuple:
        return self.queue.pop(0)

    def push(self, t: tuple) -> None:
        self.queue.append(t)

    def is_empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
