
# @Title: 托普利茨矩阵 (Toeplitz Matrix)
# @Author: KivenC
# @Date: 2018-07-12 16:40:02
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
