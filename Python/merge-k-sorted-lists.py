#!/usr/bin/env python3

"""Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoList(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        dummy = ListNode(-1)
        p = dummy
        while True:
            if l1 == None:
                p.next = l2
                break
            elif l2 == None:
                p.next = l1
                break
            elif l1.val <= l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        res = dummy.next
        dummy.next = None
        return res


    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        ret = lists[0]
        for i in range(1, len(lists)):
            ret = self.mergeTwoList(ret, lists[i])

        return ret