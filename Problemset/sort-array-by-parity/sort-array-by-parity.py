
# @Title: 按奇偶排序数组 (Sort Array By Parity)
# @Author: KivenC
# @Date: 2018-10-25 10:27:35
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) < 2:
            return A
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A
