
# @Title: 整理字符串 (Make The String Great)
# @Author: KivenC
# @Date: 2020-08-09 10:52:51
# @Runtime: 52 ms
# @Memory: 13.7 MB

class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        stack = []
        i = 0
        while i < len(s):
            if i < len(s) - 1 and abs(ord(s[i]) - ord(s[i+1])) == 32:
                i += 2
            elif stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
                i += 1
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)
