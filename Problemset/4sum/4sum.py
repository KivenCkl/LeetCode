
# @Title: 四数之和 (4Sum)
# @Author: KivenC
# @Date: 2018-07-21 17:02:12
# @Runtime: 76 ms
# @Memory: N/A

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def NSum(nums, target, N):
            n = len(nums)
            if n < N or nums[0] * N > target or nums[-1] * N < target:
                return []
            res = []
            if N == 2:
                l, r = 0, n-1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append([nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:l += 1
                        while l < r and nums[r] == nums[r+1]:r -= 1
                return res
            else:
                for i in range(n-N+1):
                    # 核心，保证了两轮解中不包含重复解
                    if i == 0 or nums[i] != nums[i-1]:
                        for pre in NSum(nums[i+1:], target-nums[i], N-1):
                            res.append([nums[i]] + pre)  
                return res
            
        return NSum(sorted(nums),target,4)
