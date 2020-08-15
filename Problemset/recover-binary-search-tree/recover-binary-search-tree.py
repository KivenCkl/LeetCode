
# @Title: 恢复二叉搜索树 (Recover Binary Search Tree)
# @Author: KivenC
# @Date: 2020-08-08 19:09:34
# @Runtime: 88 ms
# @Memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 利用中序遍历找到被交换的两个节点
        stack = []  # 用于记录遍历的节点
        pre = None  # 记录当前节点的前一个节点
        x, y = None, None  # 记录两个错误的节点

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            # 找两个被交换的节点
            if pre and pre.val > root.val:
                if x is None:
                    x = pre
                y = root

            pre, root = root, root.right
        
        x.val, y.val = y.val, x.val

