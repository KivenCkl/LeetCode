
# @Title: 三数之和 (3Sum)
# @Author: KivenC
# @Date: 2018-07-21 16:31:38
# @Runtime: 1812 ms
# @Memory: N/A

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for cur in range(len(nums)-2):
            if cur > 0 and nums[cur] == nums[cur-1]:
                continue
            target = 0 - nums[cur]
            left, right = cur + 1, len(nums) -1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[cur], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res
