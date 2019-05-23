
# @Title: 跳跃游戏 (Jump Game)
# @Author: KivenC
# @Date: 2018-07-28 21:51:23
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False
        temp = nums[0]
        for i in range(1, len(nums)):
            if temp < i:
                return False
            temp = max(temp, nums[i] + i)
            if temp >= len(nums)-1:
                return True
        return temp >= len(nums)-1
