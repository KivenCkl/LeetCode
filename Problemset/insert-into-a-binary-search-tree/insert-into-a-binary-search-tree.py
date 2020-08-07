
# @Title: 二叉搜索树中的插入操作 (Insert into a Binary Search Tree)
# @Author: KivenC
# @Date: 2020-08-07 15:54:27
# @Runtime: 216 ms
# @Memory: 16 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

