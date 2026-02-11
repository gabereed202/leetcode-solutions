"""
Description: https://leetcode.com/problems/word-search/description/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
    vertically neighboring. The same letter cell may not be used more than once.



Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""

class Solution:
    """
    Solution logic:
        Loop over the board until we match with the first letter of the word.
        When we match with the first letter, we enter a recursive depth first search for the rest of the
            word starting from that point.
        We temporarily replace the current letter on the board with a marker so we don't accidentally repeat
            the same letter on the board.
        We check all four directions for a matching letter, then make a recursive call if we do find it.
    """
    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if recursive_search(board, word[1:], row, col):
                        return True

        return False


def recursive_search(board, word, row, col):
    if len(word) <= 0:
        return True

    temp = board[row][col]
    board[row][col] = '#'

    # check above
    if row >= 1 and board[row - 1][col] == word[0]:
        if recursive_search(board, word[1:], row - 1, col):
            return True

    # check right
    if col <= len(board[row]) - 2 and board[row][col + 1] == word[0]:
        if recursive_search(board, word[1:], row, col + 1):
            return True

    # check below
    if row <= len(board) - 2 and board[row + 1][col] == word[0]:
        if recursive_search(board, word[1:], row + 1, col):
            return True

    # check left
    if col >= 1 and board[row][col - 1] == word[0]:
        if recursive_search(board, word[1:], row, col - 1):
            return True

    board[row][col] = temp

    return False
