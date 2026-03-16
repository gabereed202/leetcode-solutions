"""
Description: https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
    which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

class Solution:
    """
    Solution logic:
        Start from the bottom right element.
        Iterate from right to left, bottom to top and update the shortest path to the
            bottom right from each element of the grid by adding that element's weight to
            the minimum path weight below or to the right of the current node.
        We are essentially reverse engineering the path to the bottom right by calculating the shortest
            path from each node to the target.
    """
    def minPathSum(self, grid) -> int:

        results = []
        for i in range(len(grid)):
            results.append([None] * len(grid[i]))

        for y in range(len(grid) - 1, -1, -1):
            for x in range(len(grid[y]) - 1, -1, -1):
                if y < len(grid) - 1 and x < len(grid[y]) - 1:
                    results[y][x] = grid[y][x] + min(results[y + 1][x], results[y][x + 1])
                elif y >= len(grid) - 1 and x < len(grid[y]) - 1:
                    results[y][x] = grid[y][x] + results[y][x + 1]
                elif y < len(grid) - 1 and x >= len(grid[y]) - 1:
                    results[y][x] = grid[y][x] + results[y + 1][x]
                else:
                    results[y][x] = grid[y][x]

        return results[0][0]

