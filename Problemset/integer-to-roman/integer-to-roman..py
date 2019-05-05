
# @Title: 整数转罗马数字 (Integer to Roman)
# @Author: KivenC
# @Date: 2019-01-24 15:32:34
# @Runtime: 144 ms
# @Memory: 6.9 MB

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for val, symbol in zip(vals, symbols):
            while num >= val:
                ans += symbol
                num -= val
        return ans
