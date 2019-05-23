
# @Title: 优美的排列 II (Beautiful Arrangement II)
# @Author: KivenC
# @Date: 2018-08-05 20:45:40
# @Runtime: 88 ms
# @Memory: N/A

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if n <= 1 or k < 1 or n <= k:
            return []
        res = [1]
        for i, val in enumerate(range(k, 0, -1)):
            res.append(res[-1]+(-1)**i*val)
        for i in range(k+2, n+1):
            res.append(i)
        return res
