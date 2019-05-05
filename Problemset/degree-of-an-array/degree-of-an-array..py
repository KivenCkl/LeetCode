
# @Title: 数组的度 (Degree of an Array)
# @Author: KivenC
# @Date: 2018-07-14 18:45:26
# @Runtime: 72 ms
# @Memory: N/A

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        degree, res = 0, 1
        for index, num in enumerate(nums):
            if num in count:
                count[num].append(index)
            else:
                count[num] = [index]
        for list_index in count.values():
            if len(list_index) > degree:
                degree = len(list_index)
                res = list_index[-1] - list_index[0] + 1
            elif len(list_index) == degree:
                res = min(list_index[-1] - list_index[0] + 1, res)
        return res
