
# @Title: Pow(x, n) (Pow(x, n))
# @Author: KivenC
# @Date: 2019-05-07 23:01:27
# @Runtime: 52 ms
# @Memory: 13 MB

class Solution:
# way 1
#     def __init__(self):
#         self.cache = dict()
    
#     def myPow(self, x: float, n: int) -> float:
#         if n in self.cache:
#             return self.cache[n]
#         elif n == 0:
#             return 1.0
#         elif n == 1:
#             return x
#         elif n < 0:
#             return 1 / self.myPow(x, -n)
#         elif n % 2:
#             self.cache[n] = x * self.myPow(x, n - 1)
#             return self.cache[n]
#         else:
#             self.cache[n] = self.myPow(x, n / 2) * self.myPow(x, n / 2)
#             return self.cache[n]
    # way 2
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1.0
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
