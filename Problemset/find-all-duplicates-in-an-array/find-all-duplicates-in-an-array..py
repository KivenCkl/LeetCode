
# @Title: 数组中重复的数据 (Find All Duplicates in an Array)
# @Author: KivenC
# @Date: 2018-07-22 14:56:19
# @Runtime: 388 ms
# @Memory: N/A

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = 0 - nums[abs(nums[i]) - 1]
            if nums[abs(nums[i]) - 1] > 0:
                res.append(abs(nums[i]))
        return res
