"""
Description: https://leetcode.com/problems/jump-game/description/

You are given an integer array nums. You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
    which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

class Solution:
    """
    Solution logic:
        Iterate over the list and keep track of how much farther we can currently go.
        We subtract 1 from our range at each iteration.
        If the jump value at the current element is greater than our current jump range remaining, we
            update our current jump range to the value of the current element.
        If our range ever gets below 0 before we reach the end, we return false.
        If we reach the end without getting below 0 then we return true.
    """
    def canJump(self, nums) -> bool:

        if len(nums) == 1:
            return True

        jump_remaining = nums[0]

        for x in nums:

            jump_remaining -= 1

            if jump_remaining < 0:
                return False
            if x > jump_remaining:
                jump_remaining = x

        return True