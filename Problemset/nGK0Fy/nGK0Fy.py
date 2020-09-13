
# @Title: 速算机器人 (速算机器人)
# @Author: KivenC
# @Date: 2020-09-12 15:02:28
# @Runtime: 40 ms
# @Memory: 13.6 MB

class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for c in s:
            if c == 'A':
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y

