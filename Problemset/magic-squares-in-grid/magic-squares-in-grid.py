
# @Title: 矩阵中的幻方 (Magic Squares In Grid)
# @Author: KivenC
# @Date: 2018-07-17 12:55:12
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                sub_matrix = [[grid[i+ni][j+nj] for nj in range(3)] for ni in range(3)]
                if self.is_magic(sub_matrix):
                    count += 1
        return count
    def is_magic(self, matrix):
        is_number_right = all(0 < matrix[i][j] <= 9 for i in range(3) for j in range(3)) and matrix[0][0] != 5
        is_row_right = all(sum(row) == 15 for row in matrix)
        is_col_right = all(sum(col) == 15 for col in [[matrix[i][j] for i in range(3)] for j in range(3)])
        is_diag_right = matrix[1][1] == 5 and matrix[0][0] + matrix[2][2] == 10 and matrix[0][2] + matrix[2][0] == 10
        return is_number_right and is_row_right and is_col_right and is_diag_right
