
# @Title: 对角线遍历 (Diagonal Traverse)
# @Author: KivenC
# @Date: 2020-08-04 10:57:20
# @Runtime: 232 ms
# @Memory: 16.6 MB

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # # 记录每一层从右上角到左下角对角线的元素
        # # 当层数为偶数时，反转列表后添加
        # m, n, res = len(matrix), len(matrix) and len(matrix[0]), []

        # for i in range(m+n+1):
        #     tmp = [matrix[j][i-j] for j in range(max(0, i-n+1), min(i+1, m))]
        #     res += tmp if i % 2 else tmp[::-1]
        # return res

        m, n = len(matrix), len(matrix) and len(matrix[0])
        record = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                record[i+j].append(matrix[i][j])
        res = []
        for i in range(m+n+1):
            res += record[i] if i % 2 else record[i][::-1]

        return res

