
# @Title: 判断子序列 (Is Subsequence)
# @Author: KivenC
# @Date: 2020-07-27 13:46:03
# @Runtime: 40 ms
# @Memory: 13.6 MB

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        len_s, len_t = len(s), len(t)
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len_s

