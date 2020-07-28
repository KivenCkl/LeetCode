
# @Title: 第K个语法符号 (K-th Symbol in Grammar)
# @Author: KivenC
# @Date: 2020-07-21 13:20:27
# @Runtime: 40 ms
# @Memory: 13.8 MB

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return bin(K-1).count('1') % 2  # 一个 1 代表翻转过一次

