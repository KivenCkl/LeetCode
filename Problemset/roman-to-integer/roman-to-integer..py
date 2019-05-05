
# @Title: 罗马数字转整数 (Roman to Integer)
# @Author: KivenC
# @Date: 2019-01-24 22:45:42
# @Runtime: 152 ms
# @Memory: 6.9 MB

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = symbol_value.get(s[-1]) or 0
        for i in range(len(s) - 1):
            cur = symbol_value[s[i]]
            next = symbol_value[s[i + 1]]
            if cur < next:
                ans -= cur
            else:
                ans += cur
        return ans
