
# @Title: 两两交换链表中的节点 (Swap Nodes in Pairs)
# @Author: KivenC
# @Date: 2019-01-27 18:19:05
# @Runtime: 44 ms
# @Memory: 6.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        count = 1
        while cur:
            if count % 2 == 1:
                temp = cur
            else:
                if pre is None:
                    head = cur
                else:
                    pre.next = cur
                temp.next = cur.next
                cur.next = temp
                pre = temp
            count += 1
            cur = temp.next
        return head
