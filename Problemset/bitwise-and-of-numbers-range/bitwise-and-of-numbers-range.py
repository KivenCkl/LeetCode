
# @Title: 数字范围按位与 (Bitwise AND of Numbers Range)
# @Author: KivenC
# @Date: 2020-08-23 14:37:46
# @Runtime: 64 ms
# @Memory: 13.7 MB

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 给定两个整数，找到它们对应的二进制字符串的公共前缀
        # shift = 0
        # while m < n:
        #     m >>= 1
        #     n >>= 1
        #     shift += 1
        # return m << shift

        # 清除 n 最右侧的 1，直至小于 m
        while m < n:
            n &= (n - 1)
        return n

