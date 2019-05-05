
# @Title: 移除元素 (Remove Element)
# @Author: KivenC
# @Date: 2018-07-13 15:47:14
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                nums.append(-1)
                count += 1
        return len(nums) - count
