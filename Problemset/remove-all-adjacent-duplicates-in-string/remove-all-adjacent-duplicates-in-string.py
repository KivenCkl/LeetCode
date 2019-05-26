
# @Title: 删除字符串中的所有相邻重复项 (Remove All Adjacent Duplicates In String)
# @Author: KivenC
# @Date: 2019-05-26 15:37:08
# @Runtime: 92 ms
# @Memory: 13.3 MB

class Solution:
    def removeDuplicates(self, S: str) -> str:
        # 维护一个栈，将字符依次入栈，如果即将入栈的字符与栈顶元素相同，则将其出栈
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)
