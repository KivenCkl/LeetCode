
# @Title: 二叉树展开为链表 (Flatten Binary Tree to Linked List)
# @Author: KivenC
# @Date: 2020-08-02 16:11:02
# @Runtime: 44 ms
# @Memory: 14.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if not root or (not root.left and not root.right):
    #         return root
    #     # 将左右子树捋直
    #     self.flatten(root.left)
    #     self.flatten(root.right)
    #     # 把捋直的右子树进行备份
    #     tmp = root.right
    #     # 把捋直的左子树放到右边
    #     root.right = root.left
    #     # 左子树置空
    #     root.left = None
    #     # 找到现在右子树最后一个结点
    #     while root.right:
    #         root = root.right
    #     # 把捋直的原来的右子树接上去
    #     root.right = tmp

    # 右左根遍历
    def __init__(self):
        self.last = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.last
        root.left = None
        self.last = root

