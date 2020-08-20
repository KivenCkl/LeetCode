
# @Title: 有序链表转换二叉搜索树 (Convert Sorted List to Binary Search Tree)
# @Author: KivenC
# @Date: 2020-08-18 22:37:05
# @Runtime: 172 ms
# @Memory: 19.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMidNode(left: ListNode, right: ListNode) -> TreeNode:
            slow = fast = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def generateTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMidNode(left, right)
            root = TreeNode(mid.val)
            root.left = generateTree(left, mid)
            root.right = generateTree(mid.next, right)
            return root
        
        return generateTree(head, None)

