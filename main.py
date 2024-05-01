from backtracking_solver import backtracking_solver
from min_conflicts_solver import min_conflicts_solver
from sudoku import Sudoku

puzzle = Sudoku(3).difficulty(0.5)

print(puzzle.show())

result, assignments, backtracks = backtracking_solver(puzzle)
for i in range(9):
    print(f"{result[i, 0].value}  {result[i, 1].value}  {result[i, 2].value}  {result[i, 3].value}  "
          f"{result[i, 4].value}  {result[i, 5].value}  {result[i, 6].value}  {result[i, 7].value}  "
          f"{result[i, 8].value}")

print(f"Assignments made: {assignments}")
print(f"Backtracks made: {backtracks}")

result = min_conflicts_solver(puzzle, max_steps=10000, tabu_size=10)
if result is not None:
    for i in range(9):
        print(f"{result[i, 0].value}  {result[i, 1].value}  {result[i, 2].value}  {result[i, 3].value}  "
              f"{result[i, 4].value}  {result[i, 5].value}  {result[i, 6].value}  {result[i, 7].value}  "
              f"{result[i, 8].value}")
else:
    print("No result found")
