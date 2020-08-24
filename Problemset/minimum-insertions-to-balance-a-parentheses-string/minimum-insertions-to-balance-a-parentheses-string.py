
# @Title: 平衡括号字符串的最少插入次数 (Minimum Insertions to Balance a Parentheses String)
# @Author: KivenC
# @Date: 2020-08-24 22:23:59
# @Runtime: 80 ms
# @Memory: 14.1 MB

class Solution:
    def minInsertions(self, s: str) -> int:
        # # 栈模拟
        # stack = []
        # count = 0
        # for c in s:
        #     if c == '(':
        #         if stack and stack[-1] == ')':
        #             stack.pop()
        #             stack.pop()
        #             count += 1
        #         stack.append(c)
        #     elif not stack:
        #         stack += ['(', c]
        #         count += 1
        #     elif stack[-1] == '(':
        #         stack.append(c)
        #     else:  # stack[-1] == ')'
        #         stack.pop()
        #         stack.pop()
        # while stack:
        #     if stack[-1] == ')':
        #         stack.pop()
        #         stack.pop()
        #         count += 1
        #     else:
        #         stack.pop()
        #         count += 2
        # return count

        # # 计数法
        # count, n = 0, len(s)
        # left = 0  # 记录左括号个数
        # i = 0
        # while i < n:
        #     if s[i] == '(':
        #         left += 1
        #     else:
        #         if i + 1 < n and s[i+1] == ')':
        #             i += 1
        #         else:  # 缺少一个右括号
        #             count += 1
        #         if left > 0:  # 删除一个左括号
        #             left -= 1
        #         else:  # 补左括号
        #             count += 1
        #     i += 1
        # return count + left * 2

        # 替换法
        s = s.replace('))', '*')
        needcnt = s.count(')')
        s = s.replace(')', '*')

        while len(ss := s.replace('(*', '')) != len(s):
            s = ss

        return needcnt + len(s) + s.count('(')
            
