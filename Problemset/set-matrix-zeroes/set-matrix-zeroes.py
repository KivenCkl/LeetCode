
# @Title: 矩阵置零 (Set Matrix Zeroes)
# @Author: KivenC
# @Date: 2018-07-31 21:56:18
# @Runtime: 200 ms
# @Memory: N/A

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        row, col = False, False
        
        for i in range(R):
            if matrix[i][0] == 0:
                col = True
                break
        for j in range(C):
            if matrix[0][j] == 0:
                row = True
                break
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, R):
            if matrix[i][0] == 0:
                for j in range(1, C):
                    matrix[i][j] = 0
        for j in range(1, C):
            if matrix[0][j] == 0:
                for i in range(1, R):
                    matrix[i][j] = 0
        if row:
            for j in range(C):
                matrix[0][j] = 0
        if col:
            for i in range(R):
                matrix[i][0] = 0
