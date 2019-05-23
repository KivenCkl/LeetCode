
# @Title: 有效的回旋镖 (Valid Boomerang)
# @Author: KivenC
# @Date: 2019-05-08 16:47:04
# @Runtime: 52 ms
# @Memory: 12.9 MB

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x, y, z = points
        return (y[1] - x[1]) * (z[0] - x[0]) != (y[0] - x[0]) * (z[1] - x[1])
