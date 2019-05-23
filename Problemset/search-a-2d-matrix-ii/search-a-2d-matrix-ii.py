
# @Title: 搜索二维矩阵 II (Search a 2D Matrix II)
# @Author: KivenC
# @Date: 2019-03-13 13:31:44
# @Runtime: 68 ms
# @Memory: 17.8 MB

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j > -1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
