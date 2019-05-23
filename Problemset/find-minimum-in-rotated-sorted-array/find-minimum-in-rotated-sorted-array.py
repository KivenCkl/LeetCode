
# @Title: 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)
# @Author: KivenC
# @Date: 2018-07-25 17:07:54
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid
        return nums[left]
