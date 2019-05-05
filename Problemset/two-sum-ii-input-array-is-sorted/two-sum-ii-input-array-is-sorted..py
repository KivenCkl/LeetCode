
# @Title: 两数之和 II - 输入有序数组 (Two Sum II - Input array is sorted)
# @Author: KivenC
# @Date: 2018-07-14 15:01:31
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for index, num in enumerate(numbers, start=1):
            if target - num in dic:
                return [dic[target - num], index]
            else:
                dic[num] = index
        return []
