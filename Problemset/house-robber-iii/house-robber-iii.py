
# @Title: 打家劫舍 III (House Robber III)
# @Author: KivenC
# @Date: 2020-08-05 14:50:25
# @Runtime: 64 ms
# @Memory: 15.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # 我们使用一个大小为 2 的数组来表示, 0 代表不偷，1 代表偷
        # 任何一个节点能偷到的最大钱的状态可以定义为
        # 当前节点选择不偷：当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
        # 当前节点选择偷：当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数
        # 表示为公式如下
        return max(self._rob(root))
    
    def _rob(self, root: TreeNode) -> tuple:
        if not root: return 0, 0
        left = self._rob(root.left)
        right = self._rob(root.right)
        return max(left) + max(right), left[0] + right[0] + root.val

