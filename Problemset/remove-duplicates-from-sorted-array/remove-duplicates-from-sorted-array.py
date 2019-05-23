
# @Title: 删除排序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: KivenC
# @Date: 2018-07-15 12:40:20
# @Runtime: 1276 ms
# @Memory: N/A

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp, count = None, 0
        for num in nums[::-1]:
            if temp == num:
                count += 1
                nums.remove(num)
                nums.append(count)
            else:
                temp = num
        return len(nums) - count
            
