
# @Title: 缺失数字 (Missing Number)
# @Author: KivenC
# @Date: 2018-07-13 22:19:37
# @Runtime: 56 ms
# @Memory: N/A

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums.append(0)
        for index, val in enumerate(nums):
            if index != val:
                return index
