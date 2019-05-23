
# @Title: 递增的三元子序列 (Increasing Triplet Subsequence)
# @Author: KivenC
# @Date: 2019-03-15 16:56:39
# @Runtime: 84 ms
# @Memory: 13.5 MB

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        i, j = float('inf'), float('inf')
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False
