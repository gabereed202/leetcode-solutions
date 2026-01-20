"""
Description: https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check
if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""

# Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Solution logic:
        Recursively call this method for the left and right children of the current node
        in both trees until the nodes' values are not equal, or they are both null.

        If they are both null, return true, else return false. This works because we need both
        the left and right subtrees at all steps to evaluate to true in order for the final
        result to be true.
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)