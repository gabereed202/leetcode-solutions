"""
Description: https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
    down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
    bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
"""

class Solution:
    """
    Solution logic:
        The number of unique paths from each cell to the finish is equivalent to the sum unique paths from the
            cell to its right and the cell below it. We also know that the number of unique paths for each cell
            on the bottom row and the far right column are all one.
        With this knowledge, we can calculate the number of unique paths for each cell in reverse order,
            starting with the bottom right corner and moving towards the top left corner.

        First we initialize our grid with the following properties:
            For rows and columns from [0][0] to [m - 2][n - 2] we initialize None
            The m-1 row and n-1 column should be initialized with 1s because there is only 1 unique path
                from all of those positions.
            We add a row to the bottom and a column to the right with 0s so we don't have to do any out of
                bounds checking later. This represents the space bordering the actual grid the robot traverses.
        Then we ascend the rows, calculating each cell in the row from right to left before moving up a row.
        We calculate the unique paths from each cell by adding the previously calculated unique paths from the
            cells to the right and down.
        Once we have iterated over the whole grid, the answer is in the top left cell of the grid
    """
    def uniquePaths(self, m: int, n: int) -> int:

        grid = []

        for _ in range(m - 1):
            x = []
            for _ in range(n - 1):
                x.append(None)
            x.append(1)
            x.append(0)
            grid.append(x)

        grid.append([1] * n)
        grid.append([0] * n)

        for row in reversed(range(m - 1)):
            for col in reversed(range(n - 1)):
                grid[row][col] = grid[row + 1][col] + grid[row][col + 1]

        return grid[0][0]
