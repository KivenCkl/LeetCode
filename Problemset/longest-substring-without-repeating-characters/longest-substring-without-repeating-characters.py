
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: KivenC
# @Date: 2019-06-05 11:25:11
# @Runtime: 100 ms
# @Memory: 13.2 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        # 如果 s[j] 在 [i, j) 范围内有与 s[j'] 重复的字符，我们不需要逐渐增加 i
        # 我们可以直接跳过 [i，j'] 范围内的所有元素，并将 i 变为 j' + 1
        dic = dict()
        res, i = 0, 0
        for j, c in enumerate(s):
            i = max(dic.get(c, 0), i)
            res = max(res, j - i + 1)
            dic[c] = j + 1
        return res
