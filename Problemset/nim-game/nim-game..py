
# @Title: Nim 游戏 (Nim Game)
# @Author: KivenC
# @Date: 2018-12-04 15:15:56
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1,2,3 true 4 false 5,6,7 true 8 false
        assert n > 0, 'n should > 0'
        return n % 4 != 0
