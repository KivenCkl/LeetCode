
# @Title: 字符串中的第一个唯一字符 (First Unique Character in a String)
# @Author: KivenC
# @Date: 2019-03-07 15:39:35
# @Runtime: 68 ms
# @Memory: 13.1 MB

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        for i in range(len(s)):
            if s[i] not in s[:i] + s[i+1:]:
                return i
        return -1
        '''
        ans = [s.index(c) for c in set(s) if s.find(c) == s.rfind(c)]
        return min(ans) if ans else -1
