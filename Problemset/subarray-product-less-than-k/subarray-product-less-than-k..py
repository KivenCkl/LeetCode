
# @Title: 乘积小于K的子数组 (Subarray Product Less Than K)
# @Author: KivenC
# @Date: 2018-07-19 18:54:24
# @Runtime: 232 ms
# @Memory: N/A

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 滑动窗口
        if k <= 1:
            return 0
        count, mul, left = 0, 1, 0
        for i in range(len(nums)):
            mul *= nums[i]
            while mul >= k:
                mul /= nums[left]
                left += 1
            count += i - left + 1
        return count
