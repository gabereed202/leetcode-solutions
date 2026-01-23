"""
Description: https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    """
    Solution logic:
        If the number of rows is 1, we can just return s as is.
        Otherwise, we initialize a list of strings that has num_rows elements in it.
        We now iterate once over s while keeping track of what the current row of the zigzag pattern
            we are on. I.e. we should start with the first row (index: 0) and move down (down visually but
            up in index value) until we reach the bottom row (index: num_rows - 1). Then we move in the opposite direction until
            we reach the top row. All the while we are storing each character in the corresponding row element
            so that we can concatenate all the rows together at the end.
        Once all the characters have been placed into their correct row string, we loop over the rows and
            concatenate them together. This concatenated string is the result.
    """
    def convert(self, s: str, num_rows: int) -> str:

        if num_rows == 1:
            return s

        rows = []
        for x in range(num_rows):
            rows.append("")

        current_row = 0
        ascending = True
        for i in range(len(s)):
            rows[current_row] += s[i]
            if ascending is True:
                if current_row >= num_rows - 1:
                    ascending = False
                    current_row = num_rows - 2
                else:
                    current_row += 1
            else:
                if current_row <= 0:
                    ascending = True
                    current_row = 1
                else:
                    current_row -= 1

        result = ""
        for y in range(num_rows):
            result = result + rows[y]

        return result