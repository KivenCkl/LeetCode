
# @Title: 最大子序和 (Maximum Subarray)
# @Author: KivenC
# @Date: 2018-07-17 18:58:54
# @Runtime: 36 ms
# @Memory: N/A

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if max(nums) < 0:
            return max(nums)
        res, sum_max = 0, 0
        for num in nums:
            sum_max += num
            sum_max = max(sum_max, 0)
            res = max(res, sum_max)
        return res
