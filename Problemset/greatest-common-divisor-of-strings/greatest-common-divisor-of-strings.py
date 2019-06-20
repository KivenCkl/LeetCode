
# @Title: 字符串的最大公因子 (Greatest Common Divisor of Strings)
# @Author: KivenC
# @Date: 2019-06-13 20:57:21
# @Runtime: 56 ms
# @Memory: 13.1 MB

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # str1 + str2 != str2 + str1 是存在公因子的充要条件
        # 两个字符串的最大公因子的长度，必定是两个字符串长度的最大公约数，否则无法被除尽
        if str1 + str2 != str2 + str1:
            return ""
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        return str1[: gcd(len(str1), len(str2))]

