
# @Title: 两个非重叠子数组的最大和 (Maximum Sum of Two Non-Overlapping Subarrays)
# @Author: KivenC
# @Date: 2020-07-27 18:33:49
# @Runtime: 68 ms
# @Memory: 13.7 MB

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # 前缀求和 + 动态规划
        # 前缀求和方便窗口滑动
        # 可以将问题看作 A[:i] 数组中，两个子数组的元素的最大和
        for i in range(1, len(A)):
            A[i] += A[i-1]
        res, Lmax, Mmax = A[L+M-1], A[L-1], A[M-1]
        for i in range(L+M, len(A)):
            Lmax = max(Lmax, A[i-M] - A[i-L-M])
            Mmax = max(Mmax, A[i-L] - A[i-L-M])
            res = max(res, Lmax + A[i] - A[i-M], Mmax + A[i] - A[i-L])
        return res

