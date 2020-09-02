
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: KivenC
# @Date: 2020-08-26 19:01:39
# @Runtime: 52 ms
# @Memory: 13.8 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapper = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        for digit in digits:
            res = [s + c for s in res for c in mapper[digit]]
        return res

