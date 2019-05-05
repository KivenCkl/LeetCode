
# @Title: 移动零 (Move Zeroes)
# @Author: KivenC
# @Date: 2019-03-13 11:40:40
# @Runtime: 108 ms
# @Memory: 14.3 MB

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zero_index.append(i)
                i += 1
            elif zero_index:
                index = zero_index.pop(0)
                nums[index], nums[i] = nums[i], nums[index]
                zero_index.append(i)
                i += 1
            else:
                i += 1
