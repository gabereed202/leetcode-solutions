"""
Description: https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    """
    Solution logic:
        In a loop, we traverse the matrix in clock-wise rotation.
        The loop has the following rules:
            We iterate over the top row left to right, then the rightmost column top to bottom, then the bottom
                row from right to left, then the leftmost column from bottom to top, then repeat.
            At each step, we add the value of the current cell to our output list.
            After clearing the current row or column, we move the top, bottom, left and right borders towards
                the center appropriately. These borders are kept track of in variables. This is to ensure
                that we spiral inwards without traversing over the same cell more than once, and not just
                circle the outside of the matrix.
            We stop once our counter variable reaches the total number of cells in the matrix
    """
    def spiralOrder(self, matrix):
        left, top = 0, 0
        right = len(matrix[0])
        bottom = len(matrix)

        i = 0
        j = 0

        results = []

        total = right * bottom
        count = 0

        while True:
            while j < right:
                results.append(matrix[i][j])
                count += 1
                j += 1
            top += 1
            j -= 1
            if count >= total:
                break

            i += 1
            while i < bottom:
                results.append(matrix[i][j])
                count += 1
                i += 1
            right -= 1
            i -= 1
            if count >= total:
                break

            j -= 1
            while j >= left:
                results.append(matrix[i][j])
                count += 1
                j -= 1
            bottom -= 1
            j += 1
            if count >= total:
                break

            i -= 1
            while i > top:
                results.append(matrix[i][j])
                count += 1
                i -= 1
            left += 1
            if count >= total:
                break

        return results