
# @Title: 多边形三角剖分的最低得分 (Minimum Score Triangulation of Polygon)
# @Author: KivenC
# @Date: 2019-05-15 22:25:19
# @Runtime: 152 ms
# @Memory: 12.9 MB

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        # dp[i][j](0 <= i < j < n) 表示多边形 A[i]...A[j] 的最优三角剖分值
        # dp[0, n-1] = dp[0, j] + dp[j, n-1] + A[0] * A[n-1] * A[j]
        length = len(A)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length-1, -1, -1):
            for j in range(length):
                if j - i > 1:
                    dp[i][j] = float('inf')
                    for k in range(i+1, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
        return dp[0][length-1]
