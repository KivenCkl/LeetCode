
# @Title: 生成每种字符都是奇数个的字符串 (Generate a String With Characters That Have Odd Counts)
# @Author: KivenC
# @Date: 2020-07-21 15:43:11
# @Runtime: 40 ms
# @Memory: 13.8 MB

class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * n if n % 2 else 'a' * (n - 1) + 'b'

