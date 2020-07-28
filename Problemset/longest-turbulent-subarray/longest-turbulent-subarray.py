
# @Title: 最长湍流子数组 (Longest Turbulent Subarray)
# @Author: KivenC
# @Date: 2020-07-15 15:29:06
# @Runtime: 612 ms
# @Memory: 17.7 MB

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n < 2:
            return 1
        up, down, res = 1, 1, 1
        for i in range(1, n):
            if A[i] > A[i-1]:
                up, down = down + 1, 1
            elif A[i] < A[i-1]:
                down, up = up + 1, 1
            else:
                up, down = 1, 1
            res = max(res, up, down)

        return res

