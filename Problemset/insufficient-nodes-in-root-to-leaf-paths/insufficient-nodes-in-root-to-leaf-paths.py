
# @Title: 根到叶路径上的不足节点 (Insufficient Nodes in Root to Leaf Paths)
# @Author: KivenC
# @Date: 2019-06-20 10:01:31
# @Runtime: 128 ms
# @Memory: 14.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
#         # way 1
#         def _dfs(node: TreeNode, tmp: int, limit: int) -> bool:
#             """后序遍历，根据条件判断是否删除节点 node"""
#             if node.left is None and node.right is None:
#                 return node.val + tmp < limit
#             l_deleted, r_deleted = True, True
#             if node.left:
#                 l_deleted = _dfs(node.left, tmp+node.val, limit)
#             if node.right:
#                 r_deleted = _dfs(node.right, tmp+node.val, limit)
            
#             if l_deleted:
#                 node.left = None
#             if r_deleted:
#                 node.right = None
#             return l_deleted and r_deleted
        
#         if _dfs(root, 0, limit):
#             return None
#         return root

        # way 2
        def _dfs(node: TreeNode, tmp: int, limit: int) -> TreeNode:
            if node.left is None and node.right is None:
                if node.val + tmp < limit:
                    return None
                return node
            left, right = None, None
            if node.left:
                left = _dfs(node.left, tmp+node.val, limit)
            if node.right:
                right = _dfs(node.right, tmp+node.val, limit)
            if left is None and right is None:
                return None
            node.left, node.right = left, right
            return node
        
        return _dfs(root, 0, limit)
