
# @Title: 不同路径 (Unique Paths)
# @Author: KivenC
# @Date: 2018-07-29 22:15:50
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]
