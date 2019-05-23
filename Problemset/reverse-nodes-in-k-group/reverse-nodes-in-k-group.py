
# @Title: k个一组翻转链表 (Reverse Nodes in k-Group)
# @Author: KivenC
# @Date: 2019-01-27 22:17:52
# @Runtime: 104 ms
# @Memory: 7.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev, next = None, None
        cur, check = head, head
        flag, count = 0, 0
        # 检查链表长度是否满足翻转
        while flag < k and check:
            check = check.next
            flag += 1
        # 满足条件，进行翻转
        if flag == k:
            while count < k and cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                count += 1
            if next:
                # head 为链表翻转后的尾节点
                head.next = self.reverseKGroup(next, k)
            # prev 为链表翻转后的头节点
            return prev
        # 不满足翻转条件，直接返回
        else:
            return head
