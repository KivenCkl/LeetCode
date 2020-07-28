
# @Title: 最小路径和 (Minimum Path Sum)
# @Author: KivenC
# @Date: 2020-07-23 18:12:38
# @Runtime: 40 ms
# @Memory: 13.9 MB

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         tmp = float('inf')
        #         if i - 1 >= 0:
        #             tmp = min(tmp, grid[i-1][j])
        #         if j - 1 >= 0:
        #             tmp = min(tmp, grid[i][j-1])
        #         if tmp == float('inf'):
        #             tmp = 0
        #         grid[i][j] += tmp
        # return grid[-1][-1]

        dp = [float('inf')] * (len(grid[0]) + 1)
        dp[1] = 0
        for row in grid:
            for i, num in enumerate(row):
                dp[i+1] = min(dp[i], dp[i+1]) + num
        return dp[-1]

