
# @Title: 易混淆数 (Confusing Number)
# @Author: KivenC
# @Date: 2019-04-16 20:43:38
# @Runtime: 56 ms
# @Memory: 13.2 MB

class Solution:
    def confusingNumber(self, N: int) -> bool:
        dic = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        another = 0
        if N == 0:
            return False
        tmp = N
        while tmp:
            mod = tmp % 10
            if mod not in dic:
                return False
            another = 10 * another + dic[mod]
            tmp //= 10
        return N != another
