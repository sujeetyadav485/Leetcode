# Medium
# Given an m x n matrix board containing 'X' and 'O', 
# capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: 
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: 
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation: 
# Notice that an 'O' should not be flipped if:
# - It is on the border, 
# or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, 
# so it is not flipped.
# The other three 'O' form a surrounded region, 
# so they are flipped.

# Example 2:
# Input: 
# board = [["X"]]
# Output: 
# [["X"]]
 
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

# Solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        ROWS = len(board)
        COLS = len(board[0])
        borders = list(itertools.product([ROWS - 1, 0], range(COLS))) + list(itertools.product(range(ROWS), [0, COLS - 1]))

        for row, col in borders:
            self.bfs(board, row, col, ROWS, COLS)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                
                if board[i][j] == "E":
                    board[i][j] = "O"

    def bfs(self, board, row, col, ROWS, COLS):
        queue = []
        queue.append([row, col])

        while queue:
            row, col = queue.pop(0)

            if board[row][col] == "E" or board[row][col] == "X":
                continue
            
            board[row][col] = "E"

            if row + 1 < ROWS and board[row + 1][col] == "O":
                queue.append([row + 1, col])
            
            if 0 <= row - 1 and board[row - 1][col] == "O":
                queue.append([row - 1, col])
            
            if col + 1 < COLS and board[row][col + 1] == "O":
                queue.append([row, col + 1])
            
            if 0 <= col - 1 and board[row][col - 1] == "O":
                queue.append([row, col - 1])
# TC: O(m * n) SC: O(m * n)
# Accepted

            
