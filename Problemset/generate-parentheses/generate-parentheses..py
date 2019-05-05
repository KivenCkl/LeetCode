
# @Title: 括号生成 (Generate Parentheses)
# @Author: KivenC
# @Date: 2019-01-26 22:27:29
# @Runtime: 72 ms
# @Memory: 6.7 MB

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        if n == 0:
            return ['']
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    ans.append('({}){}'.format(left, right))
        return ans
