
# @Title: 最后一个单词的长度 (Length of Last Word)
# @Author: KivenC
# @Date: 2019-04-20 23:33:44
# @Runtime: 80 ms
# @Memory: 12.9 MB

'''
@Author: KivenChen
@Date: 2019-04-20
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (29.49%)
# Total Accepted:    24.1K
# Total Submissions: 81.7K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1]) if s else 0


