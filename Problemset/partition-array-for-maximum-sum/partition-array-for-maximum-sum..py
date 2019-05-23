
# @Title: 分隔数组以得到最大和 (Partition Array for Maximum Sum)
# @Author: KivenC
# @Date: 2019-05-18 23:46:56
# @Runtime: 660 ms
# @Memory: 12.9 MB

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        if n <= K:
            return max(A) * n
        if K == 1:
            return sum(A)
        dp = [0 for _ in range(n)]
        for i, a in enumerate(A):
            subarray_max = a
            # j 代表当前子数组的长度，包括 A[i]，子数组为 A[i - j + 1: i + 1]
            for j in range(1, K + 1):
                # 至少能向前构成这长度为 j 的子数组
                if i - j + 1 >= 0:
                    # 确保 subarray_max 是子数组中的最大值
                    subarray_max = max(subarray_max, A[i - j + 1])
                    
                    # A[i] 之前恰好有 j - 1 个元素，而它们一共组成了长度为 j 的子数组
                    # 相当于当前子数组可以表示为 A[:j]
                    # if i - j < 0:
                    #     dp[i] = max(dp[i], subarray_max * j)
                    # else:
                    #     dp[i] = max(dp[i], dp[i - j] + subarray_max * j)
                    dp[i] = max(dp[i], subarray_max * j + (dp[i - j] if i - j >= 0 else 0))
        return dp[-1]
