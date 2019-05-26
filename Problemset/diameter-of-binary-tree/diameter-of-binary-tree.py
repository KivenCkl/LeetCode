
# @Title: 二叉树的直径 (Diameter of Binary Tree)
# @Author: KivenC
# @Date: 2019-05-23 17:45:24
# @Runtime: 116 ms
# @Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_depth = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.depth(root)
        return self.max_depth
    
    # 在计算每个节点为根的最大深度同时保存最大直径
    # 因为最终结果不一定会过总根，所以每个结点为根都要遍历一次
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.max_depth = max(self.max_depth, l + r)
        return max(l, r) + 1
