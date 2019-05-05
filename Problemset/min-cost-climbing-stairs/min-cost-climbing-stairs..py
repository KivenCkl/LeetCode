
# @Title: 使用最小花费爬楼梯 (Min Cost Climbing Stairs)
# @Author: KivenC
# @Date: 2018-07-16 12:23:58
# @Runtime: 36 ms
# @Memory: N/A

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 1:
            return 0
        else:
            res = [0 for _ in range(len(cost)+1)]
            for i in range(2, len(res)):
                res[i] = min(res[i-2]+cost[i-2], res[i-1]+cost[i-1])
            return res[-1]
