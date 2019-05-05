
# @Title: 搜索插入位置 (Search Insert Position)
# @Author: KivenC
# @Date: 2018-07-14 14:43:42
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return i
