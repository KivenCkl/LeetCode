
# @Title: 子数组最大平均数 I (Maximum Average Subarray I)
# @Author: KivenC
# @Date: 2018-07-17 17:01:33
# @Runtime: 184 ms
# @Memory: N/A

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = sum(nums[:k])
        temp = max_sum
        for i in range(1, len(nums)-k+1):
            temp = temp - nums[i-1] + nums[i+k-1]
            max_sum = max(max_sum, temp)
        return max_sum / float(k)
