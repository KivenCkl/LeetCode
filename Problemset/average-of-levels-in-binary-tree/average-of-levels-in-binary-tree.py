
# @Title: 二叉树的层平均值 (Average of Levels in Binary Tree)
# @Author: KivenC
# @Date: 2020-09-12 10:34:37
# @Runtime: 64 ms
# @Memory: 15.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        stack = [root]
        while stack:
            new_stack = []
            res.append(sum(map(lambda x: x.val, stack)) / len(stack))
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return res

