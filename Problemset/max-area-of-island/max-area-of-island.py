
# @Title: 岛屿的最大面积 (Max Area of Island)
# @Author: KivenC
# @Date: 2018-07-18 16:06:28
# @Runtime: 88 ms
# @Memory: N/A

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    res = max(res, self.dfs(grid, r, c))
        return res
    
    def dfs(self, grid, r, c):
        R, C = len(grid), len(grid[0])
        if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
            return 0
        # 将访问过的点置零
        grid[r][c] = 0
        return 1 + self.dfs(grid, r-1, c) + self.dfs(grid, r+1, c) + self.dfs(grid, r, c-1) + self.dfs(grid, r, c+1)
