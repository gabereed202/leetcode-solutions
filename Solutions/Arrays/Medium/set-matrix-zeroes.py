"""
Description: https://leetcode.com/problems/set-matrix-zeroes/description/

Given an m x n integer matrix,
if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""


class Solution:
    """
    Solution logic:
        Traverse the matrix and check for zeroes
        Store the columns and rows where we have found zeroes
        Once traversed, we loop over the columns and rows to change
            the values in them to zero
    """
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        cols = {}
        rows = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        for row in rows:
            for x in range(len(matrix[row])):
                matrix[row][x] = 0

        for col in cols:
            for y in range(len(matrix)):
                matrix[y][col] = 0