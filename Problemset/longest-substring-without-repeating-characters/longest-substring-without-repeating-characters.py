
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: KivenC
# @Date: 2018-12-28 13:39:50
# @Runtime: 1044 ms
# @Memory: 6.6 MB

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        path = set()
        max_len = 0
        i = 0
        while i < (len(s) - max_len):
            j = i
            while j < len(s) and s[j] not in path:
                path.add(s[j])
                j += 1
            max_len = max(max_len, j - i)
            i += 1
            path.clear()
        return max_len
