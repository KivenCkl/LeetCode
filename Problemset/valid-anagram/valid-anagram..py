
# @Title: 有效的字母异位词 (Valid Anagram)
# @Author: KivenC
# @Date: 2019-03-12 16:17:17
# @Runtime: 56 ms
# @Memory: 13.4 MB

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        return sorted(s) == sorted(t)
        '''
        if len(s) != len(t):
            return False
        s_set = set(s)
        t_set = set(t)
        if s_set != t_set:
            return False
        for c in s_set:
            if s.count(c) != t.count(c):
                return False
        return True
