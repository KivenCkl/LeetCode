
# @Title: 不相交的线 (Uncrossed Lines)
# @Author: KivenC
# @Date: 2019-05-26 15:03:36
# @Runtime: 264 ms
# @Memory: 13.4 MB

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # 设 A[0] ~ A[x] 与 B[0] ~ B[y] 的最大连线数为 dp[x, y]，那么对于任意位置的 dp[i, j] 而言：
        # 如果 A[i] == B[j]，即 A[i] 和 B[j] 可连线，此时 dp[i, j] = dp[i - 1, j - 1] + 1
        # 如果 A[i] != B[j]，即 A[i] 和 B[j] 不可连线，此时最大连线数取决于 dp[i - 1, j] 和 dp[i, j - 1] 的较大值
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                if a == b:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
