import numpy as np
from ac3 import ac3
from cell import Cell


# Sudoku board
b = np.empty((9, 9), dtype=Cell)

# Initialize each element with a new Cell object
for i in range(9):
    for j in range(9):
        b[i, j] = Cell()

b[0, 0].set_value(1)
b[0, 1].set_value(2)
b[0, 2].set_value(3)
b[1, 0].set_value(4)
b[1, 1].set_value(5)
b[1, 2].set_value(6)
b[2, 0].set_value(7)
b[2, 1].set_value(8)
ac3(b)
print(b[2, 2].domain)  # Expecting [9]
