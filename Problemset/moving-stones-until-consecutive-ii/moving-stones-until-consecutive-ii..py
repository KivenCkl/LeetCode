
# @Title: 移动石子直到连续 II (Moving Stones Until Consecutive II)
# @Author: KivenC
# @Date: 2019-05-16 21:27:43
# @Runtime: 96 ms
# @Memory: 13.8 MB

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        # 最大值实际上是要选择将石头往最大的端点连续延伸，还是往最小的端点连续延伸
        # 能延伸的空间范围是 [0, n-1) 和 [1, n)
        # 这两端中间每个相邻石头差值之和最大者即为答案
        mind, maxd = float('inf'), max(stones[n - 1] - stones[1] + 1, stones[n - 2] - stones[0] + 1) - (n - 1)
        
        # 最小值是要找到一个连续段，这个段内每个相邻石头间的差值之和可以满足放下这个段之外的所有石头
        # 找到一个连续段的长度是 m，即范围是 [i, i + m - 1]
        # 假如这个段 ∑(stones[i] - stones[i-1]) >= n - m，则这个段可以通过规则变成连续的
        # 需要找到最小的 n - m
        # 例外，类似于 [1, 2, 5] 只有一个端点不连续序列，只需要变换两次，会比 n - m 多一次
        j = 0
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] < n:
                j += 1
            
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                cost = 2
            else:
                cost = n - (j - i + 1)
            mind = min(mind, cost)
        
        return [mind, maxd]
