
# @Title: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
# @Author: KivenC
# @Date: 2018-07-13 23:43:20
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        buy = prices[0]
        for price in prices[1:]:
            buy = min(buy, price)
            max_profit = max(max_profit, price - buy)
        return max_profit
