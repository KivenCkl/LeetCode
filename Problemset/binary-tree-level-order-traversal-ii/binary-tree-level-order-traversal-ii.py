
# @Title: 二叉树的层次遍历 II (Binary Tree Level Order Traversal II)
# @Author: KivenC
# @Date: 2020-09-06 23:38:59
# @Runtime: 40 ms
# @Memory: 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque([root])
        while queue:
            tmp = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res[::-1]
        
