
# @Title: 旋转图像 (Rotate Image)
# @Author: KivenC
# @Date: 2018-07-19 16:23:46
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
