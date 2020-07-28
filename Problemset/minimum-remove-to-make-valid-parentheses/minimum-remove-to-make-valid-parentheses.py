
# @Title: 移除无效的括号 (Minimum Remove to Make Valid Parentheses)
# @Author: KivenC
# @Date: 2020-07-20 18:44:43
# @Runtime: 108 ms
# @Memory: 15.7 MB

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        queue = []
        backet = []
        i = 0
        for c in s:
            queue.append(c)
            if c == '(':
               backet.append(i)
            elif c == ')':
                if backet:
                    backet.pop()
                else:
                    queue.pop()
                    i -= 1
            i += 1
        for i in backet[::-1]:
            queue.pop(i)
        return "".join(queue)

