
# @Title: 最接近的三数之和 (3Sum Closest)
# @Author: KivenC
# @Date: 2018-07-26 18:11:26
# @Runtime: 228 ms
# @Memory: N/A

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                temp = nums[i] +nums[left] + nums[right]
                res = temp if abs(temp-target) < abs(res-target) else res
                if temp < target:
                    left += 1
                elif temp > target:
                    right -= 1
                else:
                    return target
        return res
