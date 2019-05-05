
# @Title: 有效的括号 (Valid Parentheses)
# @Author: KivenC
# @Date: 2019-01-26 13:54:57
# @Runtime: 52 ms
# @Memory: 6.4 MB

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapper = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in mapper:
                top_element = stack.pop() if stack else '#'
                if mapper[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
        
