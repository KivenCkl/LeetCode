
# @Title: 旋转数组 (Rotate Array)
# @Author: KivenC
# @Date: 2019-03-14 16:57:56
# @Runtime: 124 ms
# @Memory: 13.4 MB

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        k = k % len(nums)
        while k > 0:
            num = nums.pop()
            nums.insert(0, num)
            k -= 1
        '''
        k = k % len(nums)
        if k > 0:
            nums.reverse()
            nums[:k] = reversed(nums[:k])
            nums[k:] = reversed(nums[k:])
