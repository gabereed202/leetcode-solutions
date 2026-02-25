"""
Description: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a
    given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


class Solution:
    """
    Solution logic:
        Since this needs to be done in O(log(n)) we need to use a searching algorithm.
        Conduct two binary searches that differ in that one will finish when we reach the left most occurrence of the
            target and one that will end when we find the right most occurrence of the target.
    """
    def searchRange(self, nums, target):
        return [self.binary_search(nums, target, True), self.binary_search(nums, target, False)]

    def binary_search(self, nums, target, leftLean):

        left = 0
        right = len(nums) - 1

        result = -1

        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                result = middle
                if leftLean:
                    right = middle - 1
                else:
                    left = middle + 1

        return result
