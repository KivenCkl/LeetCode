
# @Title: 最佳买卖股票时机含冷冻期 (Best Time to Buy and Sell Stock with Cooldown)
# @Author: KivenC
# @Date: 2020-07-10 16:45:21
# @Runtime: 56 ms
# @Memory: 13.8 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0
        
        # n = len(prices)
        # # f[i][0]: 第 i 天后手上持有股票的最大收益
        # # f[i][1]: 第 i 天后手上不持有股票，并且处于冷冻期中的累计最大收益
        # # f[i][2]: 第 i 天后手上不持有股票，并且不在冷冻期中的累计最大收益
        # f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        # for i in range(1, n):
        #     f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
        #     f[i][1] = f[i - 1][0] + prices[i]
        #     f[i][2] = max(f[i - 1][1], f[i - 1][2])
        
        # return max(f[n - 1][1], f[n - 1][2])

        # O(1) 版本
        n = len(prices)
        if n < 2:
            return 0
        hold, freeze, ready = -prices[0], 0, 0
        for i in range(1, n):
            new_hold = max(hold, ready-prices[i])
            new_freeze = hold + prices[i]
            new_ready = max(ready, freeze)
            hold, freeze, ready = new_hold, new_freeze, new_ready
        return max(freeze, ready)

