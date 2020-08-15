
# @Title: 字符串相乘 (Multiply Strings)
# @Author: KivenC
# @Date: 2020-08-13 13:50:49
# @Runtime: 252 ms
# @Memory: 13.5 MB

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # num1[i] 与 num2[j] 相乘的结果放在结果中的 [i+j, i+j+1]
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        mul = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                t = int(num1[i]) * int(num2[j])
                t += mul[i+j+1]  # 先加上之前的地位部分
                mul[i+j] += t //10
                mul[i+j+1] = t % 10
        return "".join(map(str, mul if mul[0] else mul[1:]))

