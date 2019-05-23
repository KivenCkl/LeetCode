
# @Title: 旋转链表 (Rotate List)
# @Author: KivenC
# @Date: 2019-04-05 23:55:23
# @Runtime: 56 ms
# @Memory: 13.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 1:
            return head
        length = 1
        temp_node = head
        last_node = head
        while last_node.next:
            length += 1
            last_node = last_node.next
        k_ = k % length
        if k_:
            while k_ < length - 1:
                temp_node = temp_node.next
                k_ += 1
            temp_node.next, last_node.next, head = None, head, temp_node.next
        return head
