"""
Description: https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


class Solution:
    """
    Solution logic:
        Start by adding one to the least significant digit at the end
        of the array.

        Then, while the last digit we added to is greater than 10, we
        set that digit to zero, move to the next digit and add one to that.

        We check if the current digit is greater than or equal to 10 after
        adding to each digit and stop if the digit is less than 10.

        In case the most significant digit is greater than 10 after
        adding 1, we add a leading zero at the beginning of the array.
        We don't include the 0th element of the returned array if
        it is still zero at the end of the process.
    """
    def plusOne(self, digits):

        results = [0] + digits
        current = len(results) - 1

        results[current] = results[current] + 1

        while results[current] >= 10:
            results[current] = 0
            current -= 1
            results[current] += 1

        if results[0] == 0:
            return results[1:]
        else:
            return results