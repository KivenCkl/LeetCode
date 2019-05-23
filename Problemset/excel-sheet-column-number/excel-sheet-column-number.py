
# @Title: Excel表列序号 (Excel Sheet Column Number)
# @Author: KivenC
# @Date: 2019-03-26 18:27:23
# @Runtime: 76 ms
# @Memory: 13.2 MB

class Solution:
    def titleToNumber(self, s: str) -> int:
        # mapper = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
        # res = 0
        # for i, c in enumerate(s[::-1]):
        #     res += 26 ** i * mapper[c]
        # return res
        res = 0
        for c in s:
            res *= 26
            res += ord(c) - ord('A') + 1
        return res
