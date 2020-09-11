
# @Title: 第k个排列 (Permutation Sequence)
# @Author: KivenC
# @Date: 2020-09-06 02:00:17
# @Runtime: 44 ms
# @Memory: 13.6 MB

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        candidate = [str(i) for i in range(1, n+1)]
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * i)
        res = ""
        for factorial in reversed(factorials):
            res += candidate.pop((k-1) // factorial)
            k = k % factorial
        return res
        
