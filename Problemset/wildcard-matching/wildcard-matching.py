
# @Title: 通配符匹配 (Wildcard Matching)
# @Author: KivenC
# @Date: 2019-02-28 15:10:25
# @Runtime: 276 ms
# @Memory: 13.4 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''双指针法'''
        ind_s, ind_p, match_star, ind_star = 0, 0, 0, -1
        while ind_s < len(s):
            if ind_p < len(p) and (s[ind_s] == p[ind_p] or p[ind_p] == '?'):
                ind_s += 1
                ind_p += 1
            elif ind_p < len(p) and p[ind_p] == '*':
                ind_star = ind_p
                match_star = ind_s
                ind_p += 1
            elif ind_star != -1:
                ind_p = ind_star + 1
                match_star += 1
                ind_s = match_star
            else:
                return False
        while ind_p < len(p) and p[ind_p] == '*':
            ind_p += 1
        return ind_p == len(p)
