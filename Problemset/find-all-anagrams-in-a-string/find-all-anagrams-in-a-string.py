
# @Title: 找到字符串中所有字母异位词 (Find All Anagrams in a String)
# @Author: KivenC
# @Date: 2019-05-26 23:56:17
# @Runtime: 168 ms
# @Memory: 13.9 MB

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 用哈希表记录 p 串中每个字母的出现次数，在串 s 每个允许的子串上判断每个字母的出现次数一不一样
        if len(s) < len(p):
            return []
        res = []
        k = len(p)
        record = [0 for _ in range(26)]
        for i in range(k):  # 记录字符串 p 中每个字母出现次数
            record[ord(p[i]) - ord('a')] += 1
        for i in range(len(s)):
            record[ord(s[i]) - ord('a')] -= 1
            if i >= k:  # 当 i 大于字符串 p 的长度时，要保证考虑的子串长度和 p 相同
                record[ord(s[i - k]) - ord('a')] += 1
            if record == [0] * 26:
                res.append(i + 1 - k)
        return res
