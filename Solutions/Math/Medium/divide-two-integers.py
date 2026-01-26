"""
Description: https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be
    truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed
    integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1,
    then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


class Solution:
    """
    Solution logic:
        Make both dividend and divisor positive so we can do subtraction logic but keep track of whether the
            result needs to be negative or not.
        We will subtract multiples of the divisor from the dividend until the dividend is less than 0.
        We keep track of the multiple of the divisor we subtract from the dividend and add that to our result.
        If the multiplied divisor is greater than the remaining dividend, then we subtract that from the dividend
            and start again with the multiple of 1.
        This process is repeated until the dividend is less than 0.
        We need to apply our negative value to the result without multiplying and cap the result and the
            min and max value.
    """
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        negative = 1

        if dividend < 0:
            dividend = abs(dividend)
            negative = -1
        if divisor < 0:
            divisor = abs(divisor)
            if negative == -1:
                negative = 1
            else:
                negative = -1

        dividend -= divisor
        while dividend >= 0:
            temp = divisor
            mult = 1
            while temp + temp < dividend:
                temp += temp
                mult += mult
            dividend -= temp
            result += mult

        if negative == -1:
            temp = result
            result -= temp
            result -= temp

        return check_for_max(result)

def check_for_max(result):
    if result >= 2147483648:
        return 2147483647
    elif result <= -2147483648:
        return -2147483648
    return result
