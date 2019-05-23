
# @Title: 组合总和 III (Combination Sum III)
# @Author: KivenC
# @Date: 2018-07-21 18:32:04
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, 10)]
        def kSum(nums, k, n):
            length = len(nums)
            if k < 0 or k > 9 or sum(nums[i] for i in range(k)) > n or sum(nums[i] for i in range(length-1, length-1-k, -1)) < n:
                return []
            res = []
            if k == 1:
                return res.append([n])
            elif k == 2:
                l, r = 0, length-1
                while l < r:
                    if nums[l] + nums[r] < n:
                        l += 1
                    elif nums[l] + nums[r] > n:
                        r -= 1
                    else:
                        res.append([nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                        while r > l and nums[r] == nums[r+1]: r -= 1
                return res
            else:
                for i in range(length-k+1):
                    for pre in kSum(nums[i+1:], k-1, n-nums[i]):
                        res.append([nums[i]] + pre)
                return res
        return kSum(nums, k, n)
