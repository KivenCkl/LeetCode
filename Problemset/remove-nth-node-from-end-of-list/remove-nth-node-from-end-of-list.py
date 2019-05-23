
# @Title: 删除链表的倒数第N个节点 (Remove Nth Node From End of List)
# @Author: KivenC
# @Date: 2019-01-26 13:14:26
# @Runtime: 48 ms
# @Memory: 6.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur, flag = head, head
        while n > 0:
            flag = flag.next
            n -= 1
        if not flag:
            return head.next
        while flag.next:
            cur = cur.next
            flag = flag.next
        cur.next = cur.next.next
        return head
