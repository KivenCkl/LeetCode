
# @Title: 子集 II (Subsets II)
# @Author: KivenC
# @Date: 2018-07-25 15:22:43
# @Runtime: 52 ms
# @Memory: N/A

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        temp = 0
        for i in range(len(nums)):
            start = temp if i > 0 and nums[i] == nums[i-1] else 0
            temp = len(res)
            res += [item + [nums[i]] for item in res[start:]]
        return res
