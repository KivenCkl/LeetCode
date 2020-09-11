
# @Title: N 皇后 (N-Queens)
# @Author: KivenC
# @Date: 2020-09-03 22:09:08
# @Runtime: 68 ms
# @Memory: 14 MB

class Solution:
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     # 回溯
    #     # 利用三个集合记录皇后的位置
    #     self.col = set()
    #     self.diag_1 = set()
    #     self.diag_2 = set()
    #     self.res = []
    #     self.queens = [-1] * n
    #     self.row = ["."] * n

    #     self.backtrack(0, n)
    #     return self.res
    
    # def generateGrid(self):
    #     grid = []
    #     for queen in self.queens:
    #         self.row[queen] = "Q"
    #         grid.append("".join(self.row))
    #         self.row[queen] = "."
    #     return grid
    
    # def backtrack(self, i: int, n: int):
    #     if i == n:
    #         self.res.append(self.generateGrid())
    #     else:
    #         for j in range(n):
    #             if j in self.col or j - i in self.diag_1 or j + i in self.diag_2:
    #                 continue
    #             self.queens[i] = j
    #             self.col.add(j)
    #             self.diag_1.add(j - i)
    #             self.diag_2.add(j + i)
    #             self.backtrack(i+1, n)
    #             self.col.remove(j)
    #             self.diag_1.remove(j - i)
    #             self.diag_2.remove(j + i)

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def helper(col, pie, na):
            if len(col) == n:
                result.append(col)
                return
            for i in range(n):
                if i not in col and i-len(col) not in pie and i+len(col) not in na:
                    helper(col+[i], pie+[i-len(col)], na+[i+len(col)])
        helper([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in r] for r in result]

