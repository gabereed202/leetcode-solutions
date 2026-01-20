"""
Description:

You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with
the x-axis form a container, such that the container contains the most water. Return the maximum
amount of water a container can store. Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution:
    """
    Solution logic:
        Start with one pointer at the beginning of the list and one at the end of the list.
        While the pointers have not passed each other do the following:
            1. Check if the current volume of water is greater than previous max volume
            2. Check the height at both points and move the pointer with the shorter
                height towards the other pointer
        Return the max volume found
    """
    def maxArea(self, height) -> int:

        left = 0
        right = len(height) - 1
        result = 0

        while right > left:

            h = min(height[left], height[right])
            volume = h * (right - left)
            if volume > result:
                result = volume

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return result