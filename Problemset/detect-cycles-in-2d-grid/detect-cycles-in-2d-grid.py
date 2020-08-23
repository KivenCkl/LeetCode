
# @Title: 二维网格图中探测环 (Detect Cycles in 2D Grid)
# @Author: KivenC
# @Date: 2020-08-23 00:48:18
# @Runtime: 1100 ms
# @Memory: 72 MB

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = {}
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        def bfs(i, j):
            stack = collections.deque([(i, j)])
            visited[(i, j)] = (-1, -1)
            while stack:
                i, j = stack.popleft()
                for d_i, d_j in direction:
                    ii = i + d_i
                    jj = j + d_j
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) != visited[(i, j)] and grid[ii][jj] == grid[i][j]:
                        if (ii, jj) in visited:
                            return True
                        stack.append((ii, jj))
                        visited[(ii, jj)] = (i, j)
            return False
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if bfs(i, j):
                        return True
        return False
                            
                
