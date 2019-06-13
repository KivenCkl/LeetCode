
# @Title: 有序数组中的缺失元素 (Missing Element in Sorted Array)
# @Author: KivenC
# @Date: 2019-05-06 11:48:29
# @Runtime: 100 ms
# @Memory: 17.4 MB

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(len(nums) - 1):
            gap = nums[i+1] - nums[i] - 1
            if k <= gap:
                return nums[i] + k
            k -= gap
        return nums[-1] + k
