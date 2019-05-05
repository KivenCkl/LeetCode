
# @Title: 删除排序数组中的重复项 II (Remove Duplicates from Sorted Array II)
# @Author: KivenC
# @Date: 2018-08-01 22:04:35
# @Runtime: 80 ms
# @Memory: N/A

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """            
        if len(nums) < 2:
            return len(nums)
        index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1
        return index
