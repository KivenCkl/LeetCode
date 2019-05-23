
# @Title: 反转链表 (Reverse Linked List)
# @Author: KivenC
# @Date: 2018-12-04 22:34:37
# @Runtime: 56 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head.next
        pre = head
        head.next = None
        return self._reverse(pre, cur)
    def _reverse(self, pre, cur):
        if not cur:
            return pre
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        return self._reverse(pre, cur)
