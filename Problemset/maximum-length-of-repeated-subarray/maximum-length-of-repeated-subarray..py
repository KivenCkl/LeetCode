
# @Title: 最长重复子数组 (Maximum Length of Repeated Subarray)
# @Author: KivenC
# @Date: 2018-08-02 21:50:34
# @Runtime: 6840 ms
# @Memory: N/A

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        ans = 0
        dp = [0 for _ in range(len(B) + 1)]
        for i in range(1, len(A)+1):
            for j in range(len(B), 0, -1):
                dp[j] = dp[j-1] + 1 if A[i-1] == B[j-1] else 0
                ans = max(ans, dp[j])
        return ans
