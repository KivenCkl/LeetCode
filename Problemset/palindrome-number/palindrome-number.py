
# @Title: 回文数 (Palindrome Number)
# @Author: KivenC
# @Date: 2018-12-05 22:16:28
# @Runtime: 416 ms
# @Memory: 12.2 MB

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reversed_x = 0
        original_x = x
        while x:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
        return reversed_x == original_x
