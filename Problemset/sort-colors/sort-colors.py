
# @Title: 颜色分类 (Sort Colors)
# @Author: KivenC
# @Date: 2018-07-25 15:53:32
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                length -= 1
            else:
                i += 1
