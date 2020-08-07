
# @Title: 整数拆分 (Integer Break)
# @Author: KivenC
# @Date: 2020-07-30 18:33:16
# @Runtime: 36 ms
# @Memory: 13.8 MB

class Solution:
    def integerBreak(self, n: int) -> int:
        # # 动态规划
        # if n < 4:
        #     return n - 1
        # dp = [0, 1, 2, 3] + [0] * (n-3)
        # for i in range(4, n+1):
        #     dp[i] = max(dp[j] * dp[i-j] for j in range(1, i))
        # return dp[-1]

        # 数学方法
        if n < 4:
            return n - 1
        x, y = divmod(n, 3)
        if y == 0:
            return int(math.pow(3, x))
        elif y == 1:
            return int(math.pow(3, x-1) * 4)
        else:
            return int(math.pow(3, x) * 2)

