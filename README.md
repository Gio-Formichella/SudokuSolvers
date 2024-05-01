# Sudoku Solver

This project implements two different solvers for Sudoku puzzles: a backtracking search solver and a min-conflicts local
search solver. Sudoku is a popular puzzle game where the objective is to fill a 9×9 grid with digits so that each
column, each row, and each of the nine 3×3 subgrids contains all of the digits from 1 to 9.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage and examples](#usage-and-examples)
- [Contributing](#contributing)
- [References](#references)

## Overview

Sudoku puzzles can be solved using various algorithms, and this project implements two different approaches:

1. **Backtracking Search Solver**: This solver uses a recursive backtracking algorithm to explore the solution space of
   the Sudoku puzzle. It systematically fills in empty cells with possible digits, backtracking when a dead-end is
   reached, until a valid solution is found.

2. **Min-Conflicts Local Search Solver**: This solver employs the min-conflicts local search algorithm to iteratively
   improve the current state of the Sudoku puzzle. It randomly assigns values to empty cells and then iteratively
   selects variables to improve until either a valid solution is found or a termination criterion is met. The
   implementation uses tabu search to navigate threw possible plateaus.

## Features

- Supports solving Sudoku puzzles of any difficulty level.
- Provides two different solving algorithms for comparison and experimentation.

## Installation

To use the Sudoku Solver, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Gio-Formichella/SudokuSolvers.git
    ```

2. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage and examples

Usage and examples can be found in the main.py file

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or submit a pull
request.

## References

- Russell and Norvig, *Artificial Intelligence: A Modern Approach*, 4th edition, Pearson.
