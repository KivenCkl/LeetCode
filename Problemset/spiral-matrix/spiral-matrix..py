
# @Title: 螺旋矩阵 (Spiral Matrix)
# @Author: KivenC
# @Date: 2018-07-23 19:08:23
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        res = []
        R, C = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, C-1, 0, R-1
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, bottom):
                res.append(matrix[i][right])
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        if left == right and top < bottom:
            for i in range(top, bottom+1):
                res.append(matrix[i][left])
        elif top == bottom and left < right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
        elif top == bottom and left == right:
            res.append(matrix[top][left])
        return res
