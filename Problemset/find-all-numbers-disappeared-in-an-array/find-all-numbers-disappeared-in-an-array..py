
# @Title: 找到所有数组中消失的数字 (Find All Numbers Disappeared in an Array)
# @Author: KivenC
# @Date: 2018-07-14 13:38:33
# @Runtime: 384 ms
# @Memory: N/A

class Solution(object):
    def findDisappearedNumbers(self, nums):
        self.nums=nums
        nums1=set(self.nums)
        if len(nums1)==0:
            return []
        else:
            list1=[i for i in range(1,len(self.nums)+1) if i not in nums1 ]
            return list1
