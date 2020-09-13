
# @Title: 二进制矩阵中的特殊位置 (Special Positions in a Binary Matrix)
# @Author: KivenC
# @Date: 2020-09-13 10:54:22
# @Runtime: 64 ms
# @Memory: 13.7 MB

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = [sum(r) == 1 for r in mat]
        col = [sum([mat[i][j] for i in range(m)]) == 1 for j in range(n)]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] and col[j]:
                    res += 1
        return res
        
