
# @Title: 平衡二叉树 (Balanced Binary Tree)
# @Author: KivenC
# @Date: 2020-08-17 20:11:55
# @Runtime: 60 ms
# @Memory: 18.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 自底向上递归的做法类似于后序遍历
        # 对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡
        # 如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回 -1−1
        # 如果存在一棵子树不平衡，则整个二叉树一定不平衡。
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) >= 0

