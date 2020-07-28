
# @Title: 乘积最大子数组 (Maximum Product Subarray)
# @Author: KivenC
# @Date: 2019-03-13 11:22:09
# @Runtime: 108 ms
# @Memory: 13.4 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max, local_min, global_max = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            candidates = [num, local_max * num, local_min * num]
            local_max, local_min = max(candidates), min(candidates)
            global_max = max(global_max, local_max)
        return global_max
