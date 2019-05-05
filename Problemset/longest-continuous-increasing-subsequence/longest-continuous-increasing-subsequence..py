
# @Title: 最长连续递增序列 (Longest Continuous Increasing Subsequence)
# @Author: KivenC
# @Date: 2018-07-17 19:29:09
# @Runtime: 36 ms
# @Memory: N/A

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        count, res = 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        return max(res, count)
