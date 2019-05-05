
# @Title: 杨辉三角 (Pascal's Triangle)
# @Author: KivenC
# @Date: 2018-07-12 10:48:59
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1] * i for i in range(1, numRows+1)]
        if numRows > 2:
            for i in range(2, numRows):
                triangle[i][1:-1] = [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1]) - 1)]
        return triangle
