
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: KivenC
# @Date: 2019-01-26 21:20:53
# @Runtime: 56 ms
# @Memory: 6.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        p, q, t = l1, l2, ans
        while p and q:
            if p.val <= q.val:
                t.next = ListNode(p.val)
                p = p.next
            else:
                t.next = ListNode(q.val)
                q = q.next
            t = t.next
        if not p:
            t.next = q
        if not q:
            t.next = p
        return ans.next
                
