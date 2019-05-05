
# @Title: 杨辉三角 II (Pascal's Triangle II)
# @Author: KivenC
# @Date: 2018-07-12 20:18:59
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = [[1] * i for i in range(1, rowIndex+2)]
        if rowIndex > 1:
            for i in range(2, rowIndex+1):
                triangle[i][1:-1] = [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1]) - 1)]
        return triangle[rowIndex]
