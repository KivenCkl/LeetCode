
# @Title: 格雷编码 (Gray Code)
# @Author: KivenC
# @Date: 2019-04-06 14:03:14
# @Runtime: 56 ms
# @Memory: 13.3 MB

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ''' G(i) = i ^ (i // 2)
        n = 3
        G(0) = 000
        G(1) = 1 ^ 0 = 001 ^ 000 = 001
        G(2) = 2 ^ 1 = 010 ^ 001 = 011
        G(3) = 3 ^ 1 = 011 ^ 001 = 010
        G(4) = 4 ^ 2 = 100 ^ 010 = 110
        G(5) = 5 ^ 2 = 101 ^ 010 = 111
        G(6) = 6 ^ 3 = 110 ^ 011 = 101
        G(7) = 7 ^ 3 = 111 ^ 011 = 100
        '''
        return [i ^ (i >> 1) for i in range(1 << n)]
