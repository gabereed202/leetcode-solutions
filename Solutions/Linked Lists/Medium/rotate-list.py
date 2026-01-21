"""
Description: https://leetcode.com/problems/rotate-list/description/

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution logic:
        If head is null or k is 0 we just return the head.
        Otherwise, we loop over the elements of the list until we
            reach the end to find both the tail node and the length
            of the list.
        If k is equal to the length of the list, we return the head
        Otherwise, we iterate over the list until we find the node that
            is k + 1 nodes from the tail. This is our new tail.
        We set the previous tail's next to the previous head
        We set the new head to be the new tail's next.
        We set the new end's next to None.
        Return the new head.
    """
    def rotateRight(self, head, k: int):
        if head is None or k == 0:
            return head

        length = 1
        current = head
        while current.next is not None:
            current = current.next
            length += 1

        if k == length:
            return head

        if k > length:
            k = k % length

        count = 1
        new_end = head
        while count < (length - k):
            new_end = new_end.next
            count += 1

        current.next = head
        new_head = new_end.next
        new_end.next = None

        return new_head