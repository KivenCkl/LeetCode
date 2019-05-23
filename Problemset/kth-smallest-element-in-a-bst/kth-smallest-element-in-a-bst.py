
# @Title: 二叉搜索树中第K小的元素 (Kth Smallest Element in a BST)
# @Author: KivenC
# @Date: 2019-04-06 17:05:32
# @Runtime: 76 ms
# @Memory: 17.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def gen(node):
            if node is not None:
                yield from gen(node.left)
                yield node.val
                yield from gen(node.right)
        
        it = gen(root)
        for _ in range(k):
            ans = next(it)
        return ans
