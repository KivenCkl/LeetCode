
# @Title: 搜索二维矩阵 (Search a 2D Matrix)
# @Author: KivenC
# @Date: 2018-07-30 21:19:34
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        R, C = len(matrix), len(matrix[0])
        if C < 1 or target < matrix[0][0] or target > matrix[R-1][C-1]:
            return False
        left, right = 0, R*C-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid//C][mid%C] == target:
                return True
            elif matrix[mid//C][mid%C] < target:
                left += 1
            else:
                right -= 1
        return False
