
# @Title: 高度检查器 (Height Checker)
# @Author: KivenC
# @Date: 2019-05-28 16:14:11
# @Runtime: 32 ms
# @Memory: 13.1 MB

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(i != j for i, j in zip(heights, sorted(heights)))
