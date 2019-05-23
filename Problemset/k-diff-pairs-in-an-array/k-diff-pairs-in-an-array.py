
# @Title: 数组中的K-diff数对 (K-diff Pairs in an Array)
# @Author: KivenC
# @Date: 2018-07-15 11:16:54
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            return len(set(nums) & set(num + k for num in nums))
        elif k < 0:
            return 0
        else:
            count = 0
            for num in set(nums):
                if nums.count(num) > 1:
                    count += 1
            return count
