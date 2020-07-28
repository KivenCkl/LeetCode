
# @Title: 解码方法 (Decode Ways)
# @Author: KivenC
# @Date: 2020-07-09 19:21:18
# @Runtime: 48 ms
# @Memory: 13.7 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        # if s[0] == '0':
        #     return 0
        # pre, curr = 1, 1
        # for i in range(1, len(s)):
        #     tmp = curr
        #     if s[i] == '0':
        #         if s[i-1] in "12":
        #             curr = pre
        #         else:
        #             return 0
        #     elif s[i-1] == '1' or (s[i-1] == '2' and s[i] > '0' and s[i] <= '6'):
        #             curr += pre
        #     pre = tmp
        # return curr

        if len(s) < 1 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [1, 1]
        for i in range(len(s)):
            tmp = 0 if s[i] == '0' else dp[1]
            if i > 0 and '10' <= s[i-1:i+1] <= '26':
                tmp += dp[0]
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[-1]

