
# @Title: x 的平方根 (Sqrt(x))
# @Author: KivenC
# @Date: 2019-07-16 09:51:54
# @Runtime: 52 ms
# @Memory: 13.2 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        # 牛顿法
        # 迭代公式：x_i = 1/2*(x_(i-1)+a/x_(i-1)) 
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)
