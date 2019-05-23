
# @Title: 第三大的数 (Third Maximum Number)
# @Author: KivenC
# @Date: 2018-07-17 16:27:27
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_set_nums = sorted(set(nums))
        if len(sorted_set_nums) < 3:
            return sorted_set_nums[-1]
        else:
            return sorted_set_nums[-3]
