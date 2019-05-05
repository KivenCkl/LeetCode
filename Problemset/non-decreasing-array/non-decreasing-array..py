
# @Title: 非递减数列 (Non-decreasing Array)
# @Author: KivenC
# @Date: 2018-07-17 14:04:04
# @Runtime: 52 ms
# @Memory: N/A

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count -= 1
                if i == 0 or nums[i+1] > nums[i-1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                if count < 0:
                    return False
        return True
