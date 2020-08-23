
# @Title: 你可以获得的最大硬币数目 (Maximum Number of Coins You Can Get)
# @Author: KivenC
# @Date: 2020-08-23 12:27:20
# @Runtime: 168 ms
# @Memory: 23.3 MB

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)
        return sum([piles[2 * i + 1] for i in range(len(piles) // 3)])

