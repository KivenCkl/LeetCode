
# @Title: 最长字符串链 (Longest String Chain)
# @Author: KivenC
# @Date: 2019-05-26 20:35:25
# @Runtime: 144 ms
# @Memory: 13.3 MB

class Solution:
#     # way 1
#     def longestStrChain(self, words: List[str]) -> int:
#         # 动态规划
#         # dp[i] = max(dp[i], dp[j] + 1)  (0 <= j < i 且 words[j] 是 words[i] 的前身)
#         length = len(words)
#         if length < 2:
#             return length
#         dp = [1 for _ in range(length)]
#         words.sort(key=len)  # 按字符串长度递增排序
#         for i in range(1, length):
#             if i >= 1 and words[i] == words[i - 1]:  # 去重
#                 continue
#             for j in range(i - 1, -1, -1):
#                 if len(words[i]) - len(words[j]) > 1:  # 剪枝
#                     break
#                 if len(words[i]) == len(words[j]):
#                     continue
#                 if self.isPre(words[j], words[i]):
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)
    
#     def isPre(self, word1: str, word2: str) -> bool:
#         # 判断 word1 是否是 word2 的前身
        
#         # 双指针
#         # i, j, length1, length2 = 0, 0, len(word1), len(word2)
#         # while i < length1 and j < length2:
#         #     if word1[i] == word2[j]:
#         #         i += 1
#         #     j += 1
#         # if length2 - length1 == 1 and i == length1:
#         #     return True
#         # return False
        
#         # word2 去除任意一个位置的字符后与 word1 进行比对
#         if len(word1) + 1 != len(word2):
#             return False
#         for i in range(len(word2)):
#             if word2[: i] + word2[i + 1:] == word1:
#                 return True
#         return False

    # way 2
    def longestStrChain(self, words: List[str]) -> int:
        import collections
        length = len(words)
        if length < 2:
            return length
        pool = collections.defaultdict(list)  # 将字符串按照其长度进行分组
        dp = {}
        for word in words:
            pool[len(word)].append(word)
        for key in sorted(pool.keys()):
            if key - 1 not in pool:
                continue
            for word in pool[key]:
                for j in range(key):
                    tmp = word[: j] + word[j + 1:]
                    if tmp in pool[key - 1]:
                        dp[word] = max(dp.get(word, 1), dp.get(tmp, 1) + 1)
        return max(dp.values()) if dp else 1
