
# @Title: 最小化舍入误差以满足目标 (Minimize Rounding Error to Meet Target)
# @Author: KivenC
# @Date: 2019-04-17 20:23:26
# @Runtime: 92 ms
# @Memory: 13.3 MB

import math
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        new_prices = [(math.floor(float(price)), math.ceil(float(price)) - float(price)) for price in prices]
        min_price = sum([price[0] for price in new_prices])
        new_prices = [price for price in new_prices if price[1] > 0]
        ordered_prices = sorted(new_prices, key=lambda x: abs(x[1]))
        bias = target - min_price
        if bias < 0 or bias > len(new_prices):
            return '-1'
        else:
            ans = sum([price[1] for price in ordered_prices[:bias]] + [1.0 - price[1] for price in ordered_prices[bias:]])
            return '{:.3f}'.format(ans)
                    
