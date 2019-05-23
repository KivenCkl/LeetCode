
# @Title: 买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)
# @Author: KivenC
# @Date: 2018-07-13 17:09:01
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # length of list prices should be greater than 1
        if len(prices) < 2:
            return 0
        
        buy, sell, profit = prices[0], prices[-1], 0
        prices.append(prices[-1])
        
        for i in range(1, len(prices) - 1):
            # find local min
            if prices[i] <= prices[i-1] and prices[i] < prices[i+1]:
                buy = prices[i]
            # find local max
            elif prices[i] > prices[i-1] and prices[i] >= prices[i+1]:
                sell = prices[i]
                profit += (sell - buy)
        return profit
