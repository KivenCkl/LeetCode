
# @Title: Z 字形变换 (ZigZag Conversion)
# @Author: KivenC
# @Date: 2019-01-02 09:32:30
# @Runtime: 108 ms
# @Memory: 6.7 MB

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans_string_list = [[] for _ in range(numRows)]
        length = len(s)
        period = 2 * (numRows - 1)
        for index in range(length):
            i = index % period
            if i < numRows:
                ans_string_list[i].append(s[index])
            else:
                ans_string_list[period - i].append(s[index])
        return ''.join(''.join(ans_string) for ans_string in ans_string_list)
