
# @Title: 二叉树的最大深度 (Maximum Depth of Binary Tree)
# @Author: KivenC
# @Date: 2020-07-28 10:15:30
# @Runtime: 60 ms
# @Memory: 15.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

