
# @Title: 最小路径和 (Minimum Path Sum)
# @Author: KivenC
# @Date: 2018-07-31 21:22:11
# @Runtime: 92 ms
# @Memory: N/A

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        for i in range(R):
            if i == 0:
                for j in range(1, C):
                    grid[i][j] += grid[i][j-1]
            else:
                for j in range(C):
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[R-1][C-1]
