
# @Title: 两数相加 (Add Two Numbers)
# @Author: KivenC
# @Date: 2019-06-05 10:38:34
# @Runtime: 92 ms
# @Memory: 12.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = res = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            tmp = carry
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            cur.next = ListNode(tmp % 10)
            carry = tmp // 10
            cur = cur.next
        return res.next
