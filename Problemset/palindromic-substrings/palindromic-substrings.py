
# @Title: 回文子串 (Palindromic Substrings)
# @Author: KivenC
# @Date: 2019-05-23 14:07:49
# @Runtime: 172 ms
# @Memory: 12.9 MB

class Solution:
#     way 1
    def countSubstrings(self, s: str) -> int:
        # 将每一个字符看作回文串的中心，并尝试向外扩展
        count = 0
        for i in range(len(s)):
            # 回文串长度为偶数
            count += self.expandPalindrome(s, i, i)
            # 回文串长度为奇数
            count += self.expandPalindrome(s, i, i + 1)
        return count
    
    def expandPalindrome(self, s: str, start: int, end: int) -> int:
        count = 0
        while start >=0 and end < len(s) and s[start] == s[end]:
            count += 1
            start -= 1
            end += 1
        return count
# 
#     way 2
#     def countSubstrings(self, s: str) -> int:
#         # 动态规划 dp[i] 代表 s[:i+1] 有多少回文子串
#         # dp[i] = dp[i-1] + sum([1 for index in range(i, -1, -1) if s[index:i+1] == s[index:i+1][::-1]])
#         dp = [0] * len(s)
#         dp[0] = 1
        
#         for i in range(1, len(s)):
#             dp[i] = dp[i-1] + sum([1 for index in range(i, -1, -1) if s[index:i+1] == s[index:i+1][::-1]])
            
#         return dp[-1]
