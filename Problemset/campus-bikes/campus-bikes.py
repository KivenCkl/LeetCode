
# @Title: 校园自行车分配 (Campus Bikes)
# @Author: KivenC
# @Date: 2019-04-18 08:30:01
# @Runtime: 1756 ms
# @Memory: 168.1 MB

import sys
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        m, n = len(workers), len(bikes)
        grid = [(manhattan(workers[i], bikes[j]), i, j) for j in range(n) for i in range(m)]
        ans = [0] * m
        grid = sorted(grid, key=lambda x: x[0])
        seen_x, seen_y = set(), set()
        for _, x, y in grid:
            if x not in seen_x and y not in seen_y:
                ans[x] = y
                seen_x.add(x)
                seen_y.add(y)
        return ans
        # while i:
        #     tmp_min = grid[i[0]][j[0]]
        #     record = (i[0], j[0])
        #     for ii in i:
        #         for jj in j:
        #             if grid[ii][jj] < tmp_min:
        #                 tmp_min = grid[ii][jj]
        #                 record = (ii, jj)
        #     ans.append(record)
        #     i.remove(record[0])
        #     j.remove(record[1])
        # return [record[1] for record in sorted(ans, key=lambda x: x[0])]
