
# @Title: 搜索旋转排序数组 (Search in Rotated Sorted Array)
# @Author: KivenC
# @Date: 2018-07-26 21:43:04
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
