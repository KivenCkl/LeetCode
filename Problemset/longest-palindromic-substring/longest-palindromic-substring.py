
# @Title: 最长回文子串 (Longest Palindromic Substring)
# @Author: KivenC
# @Date: 2019-06-12 15:25:33
# @Runtime: 136 ms
# @Memory: 13.1 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
#         # way 1
#         # 从回文串的中心向两边扩展，O(n^2)
#         # 分奇数串和偶数串
#         if len(s) < 2:
#             return s
        
#         def expandAroundCenter(s: str, left: int, right: int):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return right - left - 1
        
#         start, end = 0, 0
#         for i, _ in enumerate(s):
#             len_odd = expandAroundCenter(s, i, i)  # 奇数串
#             len_even = expandAroundCenter(s, i, i + 1)  # 偶数串
#             res = max(len_odd, len_even)
#             if res > end - start:
#                 start = i - (res - 1) // 2
#                 end = i + res // 2
#         return s[start: end+1]

        # way 2
        # Manacher 算法
        # O(n)
        new_s = '$#' + '#'.join(s) + '#'
        mx, ct, resLen, resCenter = 0, 0, 0, 0
        p = [0 for _ in range(len(new_s))]
        for i in range(1, len(new_s)):
            p[i] = min(p[2 * ct - i], mx - i) if mx > i else 1
            while i - p[i] >= 0 and i + p[i] < len(new_s) and new_s[i + p[i]] == new_s[i - p[i]]:
                p[i] += 1
            if mx < i + p[i] - 1:
                mx = i + p[i] - 1
                ct = i
            if resLen < p[i]:
                resLen = p[i]
                resCenter = i
        return s[(resCenter - resLen + 1) // 2:(resCenter + resLen - 1) // 2]
