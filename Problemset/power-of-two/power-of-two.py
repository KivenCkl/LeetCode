
# @Title: 2的幂 (Power of Two)
# @Author: KivenC
# @Date: 2019-04-06 16:44:18
# @Runtime: 56 ms
# @Memory: 13.2 MB

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
