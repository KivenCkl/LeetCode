
# @Title: 二叉树的所有路径 (Binary Tree Paths)
# @Author: KivenC
# @Date: 2020-09-04 22:10:59
# @Runtime: 36 ms
# @Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def helper(root, path):
            if not root:
                return
            tmp = str(root.val)
            if not root.left and not root.right:
                res.append("->".join(path + [tmp]))
            if root.left:
                helper(root.left, path + [tmp])
            if root.right:
                helper(root.right, path + [tmp])
        helper(root, [])
        return res

