
# @Title: 最后一块石头的重量 (Last Stone Weight)
# @Author: KivenC
# @Date: 2019-05-26 15:25:06
# @Runtime: 40 ms
# @Memory: 12.9 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import bisect
        stones.sort()
        while len(stones) > 1:
            a = stones.pop()
            b = stones.pop()
            if a != b:
                bisect.insort(stones, a - b)
        return stones and stones[0] or 0
