
# @Title: 搜索旋转排序数组 II (Search in Rotated Sorted Array II)
# @Author: KivenC
# @Date: 2018-07-19 22:25:10
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left = left + 1
        return False
