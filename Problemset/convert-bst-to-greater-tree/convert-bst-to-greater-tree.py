
# @Title: 把二叉搜索树转换为累加树 (Convert BST to Greater Tree)
# @Author: KivenC
# @Date: 2019-05-24 11:17:31
# @Runtime: 120 ms
# @Memory: 15.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     way 1
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         # 右-根-左顺序遍历
#         self.traversal(root, 0)
#         return root
    
#     def traversal(self, root: TreeNode, preSum: int) -> int:
#         if not root:
#             # 树为空，返回值，并将控制权交给父节点
#             return preSum
#         # 遍历右子树，返回左子树累加和，并更新当前节点的 val
#         root.val += self.traversal(root.right, preSum)
#         # 遍历左子树，并将更新后的父节点 val 传入
#         return self.traversal(root.left, root.val)
# 
#     way 2
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.preSum = 0
        
        def traversal(node):
            if not node:
                return
            traversal(node.right)
            self.preSum += node.val
            node.val = self.preSum
            traversal(node.left)
        
        traversal(root)
        return root
