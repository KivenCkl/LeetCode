
# @Title: 两数之和 (Two Sum)
# @Author: KivenC
# @Date: 2018-07-12 18:46:27
# @Runtime: 3876 ms
# @Memory: N/A

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums[i+1:], start=i+1):
                if val1 + val2 == target:
                        return [i, j]
        return 'error'
