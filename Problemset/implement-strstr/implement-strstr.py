
# @Title: 实现 strStr() (Implement strStr())
# @Author: KivenC
# @Date: 2019-01-28 14:27:13
# @Runtime: 44 ms
# @Memory: 6.5 MB

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        l_h = len(haystack)
        l_n = len(needle)
        if l_h < l_n:
            return -1
        for i in range(l_h - l_n + 1):
            if haystack[i:i+l_n] == needle:
                return i
        return -1
