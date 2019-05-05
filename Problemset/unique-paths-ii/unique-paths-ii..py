
# @Title: 不同路径 II (Unique Paths II)
# @Author: KivenC
# @Date: 2018-07-31 20:55:21
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        R = len(obstacleGrid)
        if R < 1:
            return 0
        C = len(obstacleGrid[0])
        if C < 1:
            return 0
        res = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        res[i][j] = 1
                    elif i == 0:
                        res[i][j] = res[i][j-1]
                    elif j == 0:
                        res[i][j] = res[i-1][j]
                    else:
                        res[i][j] = res[i-1][j] + res[i][j-1]
        return res[R-1][C-1]
