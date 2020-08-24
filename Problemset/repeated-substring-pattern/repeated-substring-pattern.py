
# @Title: 重复的子字符串 (Repeated Substring Pattern)
# @Author: KivenC
# @Date: 2020-08-24 21:32:30
# @Runtime: 36 ms
# @Memory: 13.8 MB

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # n = len(s)
        # for i in range(1, n//2+1):
        #     if n % i == 0 and s[:i] * (n // i) == s:
        #         return True
        # return False
        return s in (s+s)[1:-1]

