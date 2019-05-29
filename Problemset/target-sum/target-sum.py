
# @Title: 目标和 (Target Sum)
# @Author: KivenC
# @Date: 2019-05-27 11:37:56
# @Runtime: 96 ms
# @Memory: 13 MB

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         # 暴力
#         # 超时
#         res = [0]
#         for num in nums:
#             tmp = []
#             while res:
#                 preSum = res.pop()
#                 tmp.extend([preSum + num, preSum - num])
#             res = tmp
#         return sum((1 for v in res if v == S))

#         # way 1
#         # dfs 遍历所有可能结果，以当前位置 i 和当前总和 cur 为根节点
#         # 以下一位数字的加减为邻域扩散搜索
#         def dfs(cur, i, d = {}):
#             if i < len(nums) and (i, cur) not in d:  # 搜索周围节点
#                 d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
#             return d.get((i, cur), int(cur == S))
        
#         return dfs(0, 0)
    
#         # way 2
#         # 动态规划
#         # dp[i][j] 表示第 1 ~ i 个元素，和为 j 的时候，对应的方法数
#         # dp[i + 1][j] = dp[i][j - nums[i]] + dp[i][j + nums[i]]
#         sumNums = sum(nums)
#         if S > sumNums:
#             return 0
#         dp = [[0] * (2 * sumNums + 1)  for _ in range(len(nums) + 1)]
#         dp[0][0] = 1

#         for i in range(len(nums)):
#             for j in range(-sumNums, sumNums + 1):
#                 dp[i + 1][j] = dp[i][j - nums[i]] + dp[i][j + nums[i]]
#         return dp[-1][S]

        # way 3
        # 可以拆分成两部分 A, B, Sum(A) - Sum(B) = S
        # -> Sum(A) -Sum(B) + Sum(A) + Sum(B) = S + Sum(A) + Sum(B)
        # -> 2 * Sum(A) = S + Sum(A) + Sum(B)
        # -> 2 * Sum(A) = S + Sum(All)
        # -> Sum(A) = (S + Sum(All)) / 2 , S + Sum(All) 必须为偶数
        # 变成查找一个集合 A 的和等于 (S + Sum(All)) / 2
        sumNums = sum(nums)
        if S > sumNums:
            return 0
        if (S + sumNums) % 2 != 0:
            return 0
        tmp = (S + sumNums) // 2
        dp = [0] * (tmp + 1)

        dp[0] = 1
        for num in nums:
            for i in range(tmp, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]
