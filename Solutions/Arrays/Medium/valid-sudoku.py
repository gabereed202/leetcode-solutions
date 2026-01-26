"""
Description: https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
    validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

def check_number(val, group):
    if val != ".":
        elem = int(val)
        if group[elem - 1] >= 1:
            return False
        group[elem - 1] = 1
    return True


def check_square(board, rowBegin, rowEnd, colBegin, colEnd):
    group = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(rowBegin, rowEnd):
        for j in range(colBegin, colEnd):
            if not check_number(board[i][j], group):
                return False
    return True


class Solution:
    """
    Solution logic:
        Loop over the whole thing to check if the rows and columns are valid.
        Then group them by the 9 3x3 sub-boxes of the board and check if each of these
            squares are valid.
        We check rows, cols, and squares with a list where the index of each element corresponds to the
            value of found number. E.g. if we find a 5 and there is already a value in the 5th element of
            our list, then we have already seen a 5 in that row, col or square and we return false.
    """
    def isValidSudoku(self, board) -> bool:

        for i in range(9):
            group_row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            group_col = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(9):
                if not check_number(board[j][i], group_col):
                    return False
                if not check_number(board[i][j], group_row):
                    return False

        # top row
        if not check_square(board, 0, 3, 0, 3):
            return False
        if not check_square(board, 0, 3, 3, 6):
            return False
        if not check_square(board, 0, 3, 6, 9):
            return False

        # middle row
        if not check_square(board, 3, 6, 0, 3):
            return False
        if not check_square(board, 3, 6, 3, 6):
            return False
        if not check_square(board, 3, 6, 6, 9):
            return False

        # bottom row
        if not check_square(board, 6, 9, 0, 3):
            return False
        if not check_square(board, 6, 9, 3, 6):
            return False
        if not check_square(board, 6, 9, 6, 9):
            return False

        return True

