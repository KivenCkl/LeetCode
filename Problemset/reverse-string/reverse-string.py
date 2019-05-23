
# @Title: 反转字符串 (Reverse String)
# @Author: KivenC
# @Date: 2019-03-07 15:45:58
# @Runtime: 388 ms
# @Memory: 17.7 MB

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
