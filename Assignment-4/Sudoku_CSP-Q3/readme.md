# Sudoku Solver using CSP

## Description
This project implements a Sudoku solver using the Constraint Satisfaction Problem (CSP). The goal is to fill a 9×9 Sudoku grid such that all constraints are satisfied.

## CSP Formulation
- Variables: Each cell in the 9×9 grid (total 81 variables)
- Domain: Values from 1 to 9
- Constraints:
  - Each number must appear only once in every row
  - Each number must appear only once in every column
  - Each number must appear only once in every 3×3 subgrid

## Algorithm
The solution uses Backtracking Search:
1. Select an unassigned cell
2. Try all possible values (1–9)
3. Check if the assignment satisfies constraints
4. Recursively continue
5. Backtrack if no valid value is found

## Input Format
- A 9×9 grid where empty cells are represented by 0

## Output
- A completed Sudoku grid that satisfies all constraints

## How to Run
```bash
python Sudoku_CSP.py
