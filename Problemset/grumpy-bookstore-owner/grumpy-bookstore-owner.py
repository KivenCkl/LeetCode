
# @Title: 爱生气的书店老板 (Grumpy Bookstore Owner)
# @Author: KivenC
# @Date: 2019-05-28 17:54:00
# @Runtime: 92 ms
# @Memory: 14.5 MB

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        if X > n:
            return sum(customers)

        t, ans = [0] * n, 0  # t 记录老板生气时顾客数量，ans 记录不用技能的结果
        for i in range(n):
            if grumpy[i]:
                t[i] = customers[i]
            else:
                ans += customers[i]

        dp_max = dp = sum(t[: X])  # dp_max 记录技能持续时间内能增加用户的最大值，dp 用于滑动窗口
        for i in range(X, n):
            dp = dp + t[i] - t[i - X]
            dp_max = max(dp_max, dp)
        return ans + dp_max
