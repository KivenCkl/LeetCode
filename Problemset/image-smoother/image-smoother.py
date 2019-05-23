
# @Title: 图片平滑器 (Image Smoother)
# @Author: KivenC
# @Date: 2018-07-14 14:09:11
# @Runtime: 600 ms
# @Memory: N/A

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(M), len(M[0])
        res = [[0 for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                count = 0
                for i in (r-1, r, r+1):
                    for j in (c-1, c, c+1):
                        if i >= 0 and i < R and j >= 0 and j < C:
                            count += 1
                            res[r][c] += M[i][j]
                res[r][c] //= count
        return res
