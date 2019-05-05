
# @Title: 全局倒置与局部倒置 (Global and Local Inversions)
# @Author: KivenC
# @Date: 2018-07-21 12:48:30
# @Runtime: 176 ms
# @Memory: N/A

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        A_sorted = sorted(A)
        while i < len(A)-1:
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                i += 2
            else:
                i += 1
        return A == A_sorted
