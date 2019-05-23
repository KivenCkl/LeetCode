
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: KivenC
# @Date: 2019-04-06 13:31:04
# @Runtime: 52 ms
# @Memory: 13.1 MB

# def cache(func):
#     dic = {}
#     def wrapper(*arg):
#         if arg not in dic:
#             dic[arg] = func(*arg)
#         return dic[arg]
#     return wrapper

# class Solution:
#     @cache
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)
    
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
