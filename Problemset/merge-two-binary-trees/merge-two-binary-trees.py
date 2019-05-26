
# @Title: 合并二叉树 (Merge Two Binary Trees)
# @Author: KivenC
# @Date: 2019-05-23 17:02:45
# @Runtime: 108 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 递归
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        # 递归出口，选取不为 NULL 的节点直接作为新二叉树的节点
        return t1 or t2
