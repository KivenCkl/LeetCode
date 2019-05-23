
# @Title: 寻找数组的中心索引 (Find Pivot Index)
# @Author: KivenC
# @Date: 2018-07-18 15:47:09
# @Runtime: 92 ms
# @Memory: N/A

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = [0 for _ in range(len(nums))]
        right_sum = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1] if i != len(nums)-1 else 0
        for i in range(len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i-1] if i != 0 else 0
            if left_sum[i] == right_sum[i]:
                return i
        return -1
