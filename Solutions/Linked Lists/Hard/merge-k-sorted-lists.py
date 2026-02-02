"""
Description: https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Solution logic:
        This takes the list of linked lists and iterates over that list, merging the i-th list with the i+1-th list
            together by calling a helper function which is the solution from merge-two-sorted-lists.
            It will iterate over the list of lists multiple times, combining every list with the list
            next to it and reducing the number of total lists in half after each iteration, until there is
            only one list remaining.
        The single merged list that remains is our final list and we can return that list.

    """
    def mergeKLists(self, lists):
        if lists is None or len(lists) <= 0:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                one = lists[i]
                two = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(self.merge_two_lists(one, two))
            lists = merged
        return lists[0]

        return current

    def merge_two_lists(self, list1, list2):
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

