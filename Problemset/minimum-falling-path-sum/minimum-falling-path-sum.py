
# @Title: 下降路径最小和 (Minimum Falling Path Sum)
# @Author: KivenC
# @Date: 2019-10-21 10:56:29
# @Runtime: 156 ms
# @Memory: 14.1 MB

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        # 动态规划，自下而上
        while len(A) > 1:
            row = A.pop()
            for i, _ in enumerate(row):
                A[-1][i] += min(row[max(0, i - 1):min(len(row), i + 2)])
        return min(A[0])
