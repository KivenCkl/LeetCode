
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: KivenC
# @Date: 2019-01-25 10:45:25
# @Runtime: 48 ms
# @Memory: 6.5 MB

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        from functools import reduce
        
        def find_common(s1, s2):
            ans = ''
            for c1, c2 in zip(s1, s2):
                if c1 == c2:
                    ans += c1
                else:
                    break
            return ans
        if not strs:
            return ''
        return reduce(find_common, strs)
