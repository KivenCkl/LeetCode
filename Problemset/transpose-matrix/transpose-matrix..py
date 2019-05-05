
# @Title: 转置矩阵 (Transpose Matrix)
# @Author: KivenC
# @Date: 2018-07-15 10:20:17
# @Runtime: 76 ms
# @Memory: N/A

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        for i in range(0,len(A[0])):
            B.append([])
            for j in range(0,len(A)):
                B[i].append(A[j][i])
        return B        
