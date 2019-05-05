
# @Title: 三个数的最大乘积 (Maximum Product of Three Numbers)
# @Author: KivenC
# @Date: 2018-07-16 10:53:32
# @Runtime: 80 ms
# @Memory: N/A

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
