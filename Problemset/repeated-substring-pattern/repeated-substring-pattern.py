
# @Title: 重复的子字符串 (Repeated Substring Pattern)
# @Author: KivenC
# @Date: 2019-03-25 21:58:07
# @Runtime: 96 ms
# @Memory: 13.1 MB

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # length = len(s)
        # for i, c in enumerate(s, start=1):
        #     if length // i > 1 and s[:i] * (length // i) == s:
        #         return True
        # return False
        return s in (s + s)[1:-1]
