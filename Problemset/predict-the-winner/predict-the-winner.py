
# @Title: 预测赢家 (Predict the Winner)
# @Author: KivenC
# @Date: 2020-09-01 22:30:21
# @Runtime: 32 ms
# @Memory: 13.8 MB

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # n = len(nums)
        # if n % 2 == 0:  # 偶数个元素时，一定存在一种最优选择，先手选择即可
        #     return True
        # dp = [[0] * n for _ in range(n)]  # dp[i][j] 表示 num[i:j+1] 最优选择时先后手差值
        # for i in range(n-1, -1, -1):
        #     for j in range(i, n):
        #         if i == j:
        #             dp[i][j] = nums[i]
        #         else:
        #             dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        # return dp[0][n-1] >= 0

        # 空间优化
        n = len(nums)
        if n % 2 == 0:
            return True
        dp = [0] * n
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i] = nums[i]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[-1] >= 0

