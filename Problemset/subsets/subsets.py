
# @Title: 子集 (Subsets)
# @Author: KivenC
# @Date: 2018-07-12 18:11:52
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for num in nums:
            ans += [item + [num] for item in ans]
        return ans
