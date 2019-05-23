
# @Title: 两数相加 (Add Two Numbers)
# @Author: KivenC
# @Date: 2018-12-08 14:04:48
# @Runtime: 140 ms
# @Memory: 7.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = result
        while l1 or l2:
            cur.val += self.addNode(l1, l2)
            if cur.val > 9:
                cur.val -= 10
                cur.next = ListNode(1)
            else:
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result
    
    def addNode(self, node1, node2):
        if not node1 and not node2:
            pass
        if not node1:
            return node2.val
        if not node2:
            return node1.val
        return node1.val + node2.val
