
# @Title: 出现次数最多的子树元素和 (Most Frequent Subtree Sum)
# @Author: KivenC
# @Date: 2020-08-17 21:01:36
# @Runtime: 76 ms
# @Memory: 17.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        record = collections.defaultdict(int)
        def traverse(root: TreeNode) -> int:
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            tmp = root.val + left + right
            record[tmp] += 1
            return tmp
        traverse(root)
        val = max(record.values())
        return filter(lambda x: record[x] == val, record.keys())

