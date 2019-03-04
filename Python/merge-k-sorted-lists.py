#!/usr/bin/env python3

"""Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

use PriorityQueue to sort nodes
"""

from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
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


    def mergeKLists0(self, lists: 'List[ListNode]') -> 'ListNode':
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        ret = lists[0]
        for i in range(1, len(lists)):
            ret = self.mergeTwoLists(ret, lists[i])

        return ret

    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        pq = PriorityQueue()

        class wrapper:
            def __init__(self, node):
                self.node = node
                
            def __lt__(self, value):
                return value.node.val > self.node.val

        for head in lists:
            if head != None:
                pq.put(wrapper(head))

        head = ListNode(0)
        p = head
        while not pq.empty():
            node = pq.get().node
            p.next = node
            p = p.next
            node = node.next
            if node != None:
                pq.put(wrapper(node))
        return head.next


        
        
