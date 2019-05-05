
# @Title: 重塑矩阵 (Reshape the Matrix)
# @Author: KivenC
# @Date: 2018-07-11 22:37:41
# @Runtime: 128 ms
# @Memory: N/A

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        R = len(nums)
        C = len(nums[0])
        if r * c == R * C:
            temp = []
            for m, row in enumerate(nums):
                for n, val in enumerate(row):
                    if (m * C + n) % c == 0:
                        temp.append([])
                    temp[(m * C + n) // c].append(val)       
            return temp
        else:
            return nums
