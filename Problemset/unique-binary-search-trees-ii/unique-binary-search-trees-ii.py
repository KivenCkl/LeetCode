
# @Title: 不同的二叉搜索树 II (Unique Binary Search Trees II)
# @Author: KivenC
# @Date: 2020-07-21 11:16:21
# @Runtime: 72 ms
# @Memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def generateTrees(self, n: int) -> List[TreeNode]:
    #     def helper(start: int, end: int) -> List[TreeNode]:
    #         if start > end:
    #             return [None]  # 不能写为 []
    #         res = []
    #         for i in range(start, end + 1):
    #             left_trees = helper(start, i - 1)
    #             right_trees = helper(i + 1, end)
    #             for l in left_trees:
    #                 for r in right_trees:
    #                     node = TreeNode(i)
    #                     node.left = l
    #                     node.right = r
    #                     res.append(node)
    #         return res
    #     return helper(1, n) if n else []

    def generateTrees(self, n: int) -> List[TreeNode]:
        # 动态规划
        if n == 0: return []
        dp = [[] for _ in range(n+1)]
        dp[0].append(None)  # 为了 dp[0] 能够遍历
        
        for i in range(1, n+1):
            for j in range(1, i+1):
                left_num = j - 1
                right_num = i - j
                for l in dp[left_num]:
                    for r in dp[right_num]:
                        node = TreeNode(j)
                        node.left = l
                        node.right = self.clone(j, r)
                        dp[i].append(node)
        return dp[-1]
    
    def clone(self, val: int, node: TreeNode) -> TreeNode:
        if not node:
            return None
        new_node = TreeNode(node.val + val)
        new_node.left = self.clone(val, node.left)
        new_node.right = self.clone(val, node.right)
        return new_node
        
