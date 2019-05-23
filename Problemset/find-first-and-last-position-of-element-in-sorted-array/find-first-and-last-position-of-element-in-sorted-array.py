
# @Title: 在排序数组中查找元素的第一个和最后一个位置 (Find First and Last Position of Element in Sorted Array)
# @Author: KivenC
# @Date: 2018-07-27 22:12:29
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return [-1, -1]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                for i in range(mid, -1, -1):
                    if nums[i] == target: left = i 
                    else: break
                for j in range(mid, len(nums)):
                    if nums[j] == target: right = j
                    else: break
                return [left, right]
        return [-1, -1]
