
# @Title: 最大连续1的个数 (Max Consecutive Ones)
# @Author: KivenC
# @Date: 2018-07-13 15:26:28
# @Runtime: 56 ms
# @Memory: N/A

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j, max = 0, 0, 0
        nums.append(0)
        for index, val in enumerate(nums):
            if val == 0:
                j = index
                if j - i > max:
                    max = j - i
                i = j + 1
        return max
