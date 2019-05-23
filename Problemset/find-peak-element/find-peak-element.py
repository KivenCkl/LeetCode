
# @Title: 寻找峰值 (Find Peak Element)
# @Author: KivenC
# @Date: 2018-07-24 16:11:55
# @Runtime: 36 ms
# @Memory: N/A

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
