
# @Title: 路径总和 (Path Sum)
# @Author: KivenC
# @Date: 2020-07-07 17:57:00
# @Runtime: 72 ms
# @Memory: 15.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return (self.hasPathSum(root.left, sum-root.val) or 
                self.hasPathSum(root.right, sum-root.val))

