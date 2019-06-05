
# @Title: 寻找两个有序数组的中位数 (Median of Two Sorted Arrays)
# @Author: KivenC
# @Date: 2019-06-05 16:35:52
# @Runtime: 68 ms
# @Memory: 13.2 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 假设 len(A) < len(B)
        # 将 A 列表在位置 i 上划分为 left_A[:i] 和 right_A[i:]
        # 将 B 列表在位置 j 上划分为 left_B[:j] 和 right_B[j:]
        # i+j = len(A)-i+len(B)-j 且 left_A[i-1] < right_B[j] 且 left_B[j-1] < right_A[i]
        # 则 res = (max(left_part) + max(right_part)) / 2
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if n < m:
            A, B, m, n = nums2, nums1, n, m
        lo, hi, half_len = 0, m, (m + n + 1) // 2
        while lo <= hi:
            i = (lo + hi) // 2
            j = half_len - i
            if i < m and A[i] < B[j-1]:
                lo = i + 1
            elif i > 0 and B[j] < A[i-1]:
                hi = i - 1
            else:
                break
        left = max(A[i-1] if i > 0 else -float("inf"), B[j-1] if j > 0 else -float("inf"))
        if (m + n) % 2:
            return float(left)
        right = min(A[i] if i < m else float("inf"), B[j] if j < n else float("inf"))
        return (left + right) / 2

