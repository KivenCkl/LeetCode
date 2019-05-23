
# @Title: 至少是其他数字两倍的最大数 (Largest Number At Least Twice of Others)
# @Author: KivenC
# @Date: 2018-07-14 15:31:52
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        temp = sorted(nums)
        if temp[-2] != 0 and temp[-1] // temp[-2] < 2:
            return -1
        for index, num in enumerate(nums):
            if num == temp[-1]:
                return index
