
# @Title: 找出第 N 个二进制字符串中的第 K 位 (Find Kth Bit in Nth Binary String)
# @Author: KivenC
# @Date: 2020-08-09 11:05:37
# @Runtime: 48 ms
# @Memory: 13.6 MB

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return '0'
        if 2**(n-1) == k:
            return '1'
        elif k < 2**(n-1):
            return self.findKthBit(n-1, k)
        else:
            return str(1-int(self.findKthBit(n-1, 2**n - k)))
