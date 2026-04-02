class SudokuCSP:
    def __init__(self, board):
        self.board = board  
        self.size = 9

   
    def is_valid(self, row, col, num):
        # Row check
        for c in range(9):
            if self.board[row][c] == num:
                return False

        # Column check
        for r in range(9):
            if self.board[r][col] == num:
                return False

        
        start_row = row - row % 3
        start_col = col - col % 3

        for r in range(3):
            for c in range(3):
                if self.board[start_row + r][start_col + c] == num:
                    return False

        return True

    # Finding the unassigned variable 
    def find_unassigned(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return r, c
        return None

    # Backtracking algorithm part
    def solve(self):
        empty = self.find_unassigned()

        if not empty:
            return True  

        row, col = empty

        for num in range(1, 10): 
            if self.is_valid(row, col, num):
                self.board[row][col] = num  # assign

                if self.solve():  # recurse
                    return True

                self.board[row][col] = 0  # backtrack

        return False

    def print_board(self):
        for row in self.board:
            print(row)


# Example Sudoku (0 = empty)
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

sudoku = SudokuCSP(board)

if sudoku.solve():
    sudoku.print_board()
else:
    print("No solution exists")
