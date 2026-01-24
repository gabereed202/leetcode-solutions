"""
Description: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
    if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    """
    Solution logic:
        Initialize a list to be used as a stack.
        While iterating over the string, push opening parens and brackets onto the stack.
        If the closing paren or bracket appears, we pop the last element off the stack and
            check if it matches the type of closing paren or bracket we encountered. If the
            last opening paren or bracket does not match, we return false.
        If we encounter a closing paren or bracket, but the stack is empty, we return false.
        If there are elements still on the stack after iterating over the entire string, we return false.
        If we iterate over the entire string, and do not encounter any of these conditions, we return true.
    """
    def isValid(self, s: str) -> bool:

        stack = []
        for i in range(len(s)):

            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            else:
                if len(stack) <= 0:
                    return False

                last = stack.pop()

                if last == '(':
                    if s[i] != ')':
                        return False

                elif last == '[':
                    if s[i] != ']':
                        return False

                elif last == '{':
                    if s[i] != '}':
                        return False

        if len(stack) > 0:
            return False
        return True