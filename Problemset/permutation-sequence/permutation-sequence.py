
# @Title: 第k个排列 (Permutation Sequence)
# @Author: KivenC
# @Date: 2019-05-08 10:27:57
# @Runtime: 80 ms
# @Memory: 13 MB

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            return 1 if n == 0 else n * factorial(n-1)
        nums = [str(i + 1) for i in range(n)]
        total = factorial(n)
        res = ''
        while n:
            tmp = factorial(n)
            total //= n
            res += nums.pop((k - 1) // total)
            k %= total
            n -= 1
        return res
