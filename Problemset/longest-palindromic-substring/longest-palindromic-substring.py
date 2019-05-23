
# @Title: 最长回文子串 (Longest Palindromic Substring)
# @Author: KivenC
# @Date: 2018-12-28 22:16:57
# @Runtime: 216 ms
# @Memory: 6.5 MB

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
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
