
# @Title: 寻找重复数 (Find the Duplicate Number)
# @Author: KivenC
# @Date: 2018-07-22 19:46:57
# @Runtime: 52 ms
# @Memory: N/A

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            count = 0
            mid = (left + right) // 2
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left
