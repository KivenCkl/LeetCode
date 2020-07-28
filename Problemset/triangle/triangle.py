
# @Title: 三角形最小路径和 (Triangle)
# @Author: KivenC
# @Date: 2020-07-14 10:15:59
# @Runtime: 52 ms
# @Memory: 14 MB

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

