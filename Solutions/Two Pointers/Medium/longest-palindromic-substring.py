"""
Description: https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_sub = ""
        longest_len = 0

        for i in range(len(s)):

            left = i - 1
            right = i + 1
            offset_left = i
            offset_right = i + 1

            if left < 0: left = 0
            if right > len(s) - 1: right = len(s) - 1
            if offset_right > len(s) - 1: offset_right = len(s) - 1

            while left >= 0 and right < len(s) and s[left] == s[right]:

                current_len = right - left

                if current_len > longest_len:
                    longest_len = current_len
                    longest_sub = s[left:right + 1]

                left -= 1
                right += 1

            while offset_left >= 0 and offset_right < len(s) and s[offset_left] == s[offset_right]:

                current_len = offset_right - offset_left

                if current_len > longest_len:
                    longest_len = current_len
                    longest_sub = s[offset_left:offset_right + 1]

                offset_left -= 1
                offset_right += 1

        if longest_sub == "" and len(s) > 0:
            return s[0]

        return longest_sub