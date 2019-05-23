
# @Title: 删除链表中的节点 (Delete Node in a Linked List)
# @Author: KivenC
# @Date: 2018-12-04 15:28:48
# @Runtime: 52 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 将node节点的后继节点的值赋予node节点，并将其指针指向后继节点的后继节点
        # 相对于删除node节点的后继节点
        node.val = node.next.val
        node.next = node.next.next
