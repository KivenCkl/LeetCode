
# @Title: 移除盒子 (Remove Boxes)
# @Author: KivenC
# @Date: 2020-08-15 23:30:25
# @Runtime: 1236 ms
# @Memory: 96.5 MB

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        # dp[i][j][k] 表示在 [i, j] 部分能得到的最大得分
        # k 表示 boxes[i] 左边有 k 个与之相等的数可以与它结合（不需要连续）
        # 如...X DFD X DFDF X SDF [X LSKDFJ X LSJDFLK X DLKFJ...]
        # dp[i][j][k] 表示只考虑 [] 部分对分数的贡献，那么第一个 X 可能跟着前面 k 个 X 消失，也可能等着后面的 X 一起消失
        # 1. 跟前面的 k 个一起消失的话，得分为 (k + 1)**2 + helper(i+1, j, 0)
        # 2.1 跟后面的第二个 X 一起消失的话，[] 中的 "LSKDFJ" 部分独立拿分，X 成为第二个 X 开头的子序的前导之一，k -> k+1
        #     得分为 helper(i+1, m-1, 0) + helper(m, j, k+1)，m 为第二个 X 的序号
        # 2.2 跟后面的第三个 X 一起消失，[] 中的 "LSKDFJ X LSJDFLK" 部分独立拿分，X 成为第三个 X 开头的子序的前导之一
        #     k -> k + 1，得分还是 helper(i+1, m-1, 0) + helper(m, j, k+1)，m 为第三个 X 的序号
        # ...
        # 几种情况取最高得分，并存入 dp[i][j][k]

        def helper(i, j, k):
            if i > j:
                 return 0
            if dp[i][j][k] != 0:
                return dp[i][j][k]
            
            # 大段连续的部分肯定是放一起消失，而不是单个消失
            while i < j and boxes[i] == boxes[i+1]:
                i, k = i + 1, k + 1
            
            res = (k + 1)**2 + helper(i+1, j, 0)

            for m in range(i+1, j+1):
                if boxes[m] == boxes[i]:
                    res = max(res, helper(i+1, m-1, 0) + helper(m, j, k+1))
            
            dp[i][j][k] = res
            return dp[i][j][k]
        
        return helper(0, n-1, 0)

