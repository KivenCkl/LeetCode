
# @Title: 反转字符串中的单词 III (Reverse Words in a String III)
# @Author: KivenC
# @Date: 2018-12-04 15:35:18
# @Runtime: 80 ms
# @Memory: N/A

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split(' ')
        for i in range(len(sList)):
            sList[i] = sList[i][::-1]
        return ' '.join(sList)
            
