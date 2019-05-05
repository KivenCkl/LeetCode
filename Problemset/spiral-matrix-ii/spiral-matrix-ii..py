
# @Title: 螺旋矩阵 II (Spiral Matrix II)
# @Author: KivenC
# @Date: 2018-07-13 12:07:35
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, top, right, bottom, num = 0, 0, n-1, n-1, 1
        while left < right and top < bottom:
            for col in range(left, right):
                matrix[top][col] = num
                num += 1
            for row in range(top, bottom):
                matrix[row][right] = num
                num += 1
            for col in range(right, left, -1):
                matrix[bottom][col] = num
                num += 1
            for row in range(bottom, top, -1):
                matrix[row][left] = num
                num += 1
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        if n % 2 != 0:
            matrix[left][top] = num
        return matrix
