
# @Title: 反转字符串中的单词 III (Reverse Words in a String III)
# @Author: KivenC
# @Date: 2020-08-30 15:54:42
# @Runtime: 40 ms
# @Memory: 14.2 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda x: x[::-1], s.split(' ')))

