
# @Title: N叉树的层序遍历 (N-ary Tree Level Order Traversal)
# @Author: KivenC
# @Date: 2020-07-13 16:54:56
# @Runtime: 64 ms
# @Memory: 15.7 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = root and [root]
        while queue:
            yield [node.val for node in queue]
            queue = [child for node in queue for child in node.children]

