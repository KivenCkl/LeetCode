
# @Title: 根据前序和后序遍历构造二叉树 (Construct Binary Tree from Preorder and Postorder Traversal)
# @Author: KivenC
# @Date: 2020-07-08 19:08:05
# @Runtime: 60 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        L = post.index(pre[1]) + 1  # 表示左枝的长度
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root

