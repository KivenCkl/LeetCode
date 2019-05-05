
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: KivenC
# @Date: 2019-01-26 11:10:11
# @Runtime: 76 ms
# @Memory: 6.4 MB

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        num_str = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        ans = ['']
        for digit in digits:
            ans = [a + c for a in ans for c in num_str[digit]]
        return ans
