
# @Title: 分割等和子集 (Partition Equal Subset Sum)
# @Author: KivenC
# @Date: 2019-07-13 11:18:21
# @Runtime: 436 ms
# @Memory: 13 MB

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 动态规划
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
            if dp[target]:
                return True
        return False
