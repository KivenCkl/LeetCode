
# @Title: 下一个排列 (Next Permutation)
# @Author: KivenC
# @Date: 2018-07-19 21:21:29
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                flag = True
                break
        if flag:
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            for j in range(0, (len(nums) - i)//2):
                nums[i+j+1], nums[len(nums)-j-1] = nums[len(nums)-j-1], nums[i+j+1]
        else:
            nums.reverse()
