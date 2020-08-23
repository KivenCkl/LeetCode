
# @Title: 二叉树的最小深度 (Minimum Depth of Binary Tree)
# @Author: KivenC
# @Date: 2020-08-21 20:20:42
# @Runtime: 56 ms
# @Memory: 16 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def height(root: TreeNode) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            res = float('inf')
            if root.left:
                res = min(res, height(root.left))
            if root.right:
                res = min(res, height(root.right))
            return res + 1
        
        return height(root)

