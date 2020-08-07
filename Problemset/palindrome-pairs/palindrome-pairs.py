
# @Title: 回文对 (Palindrome Pairs)
# @Author: KivenC
# @Date: 2020-08-06 15:32:50
# @Runtime: 468 ms
# @Memory: 15.1 MB

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # def findWord(s: str, left: int, right: int) -> int:
        #     return indices.get(s[left:right+1], -1)
        
        # def isPalindrome(s: str, left: int, right: int) -> bool:
        #     return (sub := s[left:right+1]) == sub[::-1]
        
        # n = len(words)
        # indices = {word[::-1]: i for i, word in enumerate(words)}
        
        # ret = list()
        # for i, word in enumerate(words):
        #     m = len(word)
        #     for j in range(m + 1):
        #         if isPalindrome(word, j, m - 1):
        #             leftId = findWord(word, 0, j - 1)
        #             if leftId != -1 and leftId != i:
        #                 ret.append([i, leftId])
        #         if j and isPalindrome(word, 0, j - 1):
        #             rightId = findWord(word, j, m - 1)
        #             if rightId != -1 and rightId != i:
        #                 ret.append([rightId, i])

        # return ret

        record = {word[::-1]: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                pre, suf = word[:j], word[j:]
                if pre in record and record[pre] != i and suf[::-1] == suf:
                    res.append([i, record[pre]])
                if j > 0 and suf in record and record[suf] != i and pre[::-1] == pre:
                    res.append([record[suf], i])
        return res

