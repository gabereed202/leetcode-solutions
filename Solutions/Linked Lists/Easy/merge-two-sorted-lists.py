"""
Description: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of
    the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Solution logic:
        Create two pointers that will traverse each respective linked list and one that will
            traverse between the two lists in sorted order.
        Initialize current as the lesser of the two heads, then save current as result
            because this is the head of what will be our merged linked list.
        While at least one of the list pointers is not null we check to see which of the pointers'
            value is lesser or if one of them is null. We set current.next to the lesser or only existing node
            and then move that list pointer to the next node in that linked list. We then set current to
            current.next so that we continue on in our new linked list.
        We return result, the head of the merged linked list that we saved in the beginning.
    """
    def mergeTwoLists(self, list1, list2):
        one = list1
        two = list2

        if one is None and two is None:
            return None

        if two is None or (one is not None and one.val < two.val):
            current = one
            one = one.next
        else:
            current = two
            two = two.next

        result = current

        while one or two:

            if two is None or (one is not None and one.val < two.val):
                current.next = one
                one = one.next
            else:
                current.next = two
                two = two.next

            current = current.next

        return result


