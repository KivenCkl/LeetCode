
# @Title: 整数反转 (Reverse Integer)
# @Author: KivenC
# @Date: 2019-01-02 09:57:54
# @Runtime: 84 ms
# @Memory: 6.6 MB

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = -1 * int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        if -2 ** 31 < ans < 2 ** 31 - 1:
            return ans
        return 0
