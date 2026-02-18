"""
Description: https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
    and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

class Solution:
    """
    Solution logic:
        We take the sorted list of intervals and iterate over them, checking for overlaps.
        When we encounter an overlap, we update the end of the comparison interval and continue.
        When there is no overlap, we add the comparison interval to our results and continue.
    """
    def merge(self, intervals):

        intervals.sort()

        results = []
        comparison_interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= comparison_interval[1]:
                comparison_interval[1] = max(comparison_interval[1], intervals[i][1])
            else:
                results.append(comparison_interval)
                comparison_interval = intervals[i]

        results.append(comparison_interval)
        return results
