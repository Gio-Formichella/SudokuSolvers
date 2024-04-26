import numpy as np
from cell import Cell
from sudoku_solver import sudoku_solver

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

result = sudoku_solver(b)
for i in range(9):
    print(f"{result[i, 0].value}  {result[i, 1].value}  {result[i, 2].value}  {result[i, 3].value}  "
          f"{result[i, 4].value}  {result[i, 5].value}  {result[i, 6].value}  {result[i, 7].value}  "
          f"{result[i, 8].value}")
