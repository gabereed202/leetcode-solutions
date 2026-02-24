"""
Description: https://leetcode.com/problems/text-justification/description/

Given an array of strings words and a width maxWidth, format the text such that each line has exactly
    maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
    Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line
    does not divide evenly between words, the empty slots on the left will be assigned more spaces than the
    slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

class Solution:
    """
    Solution logic:
        We iterate over the list of words and add them to the current line if adding it to the current line
            would not exceed the maxWidth constraint.
        If we can add the word without going over the limit, we do so and move to the next word.
        We keep track of the spaces between words for later.
        If adding the current word would make the current line longer than maxWidth, we need to add the current
            line to our list of lines (results) and continue. This means we need to concatenate all of our current
            words into one line and make sure the spaces between them are correct so that the length of the line is
            equal to maxWidth.
        We add to our spaces by checking how many more characters the current line needs in order to equal maxWidth
            and then rotating through our list of spaces and adding one space to each in order until the length
            requirement is met.
        If the current word is the only one on that line, and it is the exact length of maxWidth we need to
            add special handling to make sure that it is included on the current line and that we do not include it
            on the next line as well.
        Once we are done we check if the current_line has any words on it. If it does, that means the current line
            still needs to be appended to the result list. We also need to add spaces to the end of the line so that
            the length equals maxWidth.
    """
    def fullJustify(self, words, maxWidth):

        result = []
        current_line = []
        spaces = []
        current_line_length = 0

        for word in words:
            if len(word) + current_line_length + len(spaces) + 1 > maxWidth:
                keep_word = True
                spaces_remaining = maxWidth - current_line_length - len(spaces)
                i = 0
                while len(spaces) > 0 and spaces_remaining > 0:
                    spaces[i % len(spaces)] += " "
                    spaces_remaining -= 1
                    i += 1

                if len(current_line) <= 0:
                    current_line.append(word)
                    keep_word = False

                line_string = ""
                while len(current_line) > 0:
                    line_string += current_line.pop(0)
                    if len(spaces) > 0:
                        line_string += spaces.pop(0)
                if len(line_string) < maxWidth:
                    for _ in range(maxWidth - len(line_string)):
                        line_string += " "
                result.append(line_string)
                if keep_word:
                    current_line = [word]
                    current_line_length = len(word)

            else:
                if len(current_line) > 0:
                    spaces.append(" ")
                current_line.append(word)
                current_line_length += len(word)

        if len(current_line) > 0:
            line_string = ""
            while len(current_line) > 0:
                if line_string != "":
                    line_string += " "
                line_string += current_line.pop(0)
            if len(line_string) < maxWidth:
                for _ in range(maxWidth - len(line_string)):
                    line_string += " "
            result.append(line_string)

        return result
