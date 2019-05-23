
# @Title: 验证回文串 (Valid Palindrome)
# @Author: KivenC
# @Date: 2019-03-07 15:06:51
# @Runtime: 88 ms
# @Memory: 14 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        new_s = ''
        for c in s.strip():
            if c.isalpha() or c.isdigit():
                new_s += c
        new_s = new_s.lower()
        return new_s == new_s[::-1]
        '''
        s = [c for c in s if c.isalpha() or c.isdigit()]
        if len(s) <= 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True
