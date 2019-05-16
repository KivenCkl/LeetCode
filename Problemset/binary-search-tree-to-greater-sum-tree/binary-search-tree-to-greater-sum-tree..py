
# @Title: 从二叉搜索树到更大和树 (Binary Search Tree to Greater Sum Tree)
# @Author: KivenC
# @Date: 2019-05-15 19:52:08
# @Runtime: 48 ms
# @Memory: 13 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum_value = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.bstToGst(root.right)
        root.val = self.sum_value = self.sum_value + root.val
        self.bstToGst(root.left)
        return root
