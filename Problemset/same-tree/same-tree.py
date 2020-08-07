
# @Title: 相同的树 (Same Tree)
# @Author: KivenC
# @Date: 2020-08-07 15:41:42
# @Runtime: 48 ms
# @Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
