
# @Title: 有效三角形的个数 (Valid Triangle Number)
# @Author: KivenC
# @Date: 2018-08-05 21:29:48
# @Runtime: 536 ms
# @Memory: N/A

class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        res = 0
        nums.sort()
        for i in range(2, len(nums)):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res
