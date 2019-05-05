
# @Title: 数组拆分 I (Array Partition I)
# @Author: KivenC
# @Date: 2018-07-11 17:01:30
# @Runtime: 96 ms
# @Memory: N/A

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans = ans + nums[i]
        return ans
