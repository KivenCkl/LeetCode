
# @Title: 恢复空格 (Re-Space LCCI)
# @Author: KivenC
# @Date: 2020-07-09 15:35:02
# @Runtime: 564 ms
# @Memory: 13.8 MB

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        # 动态规划，dp[i] 表示句子字串 sentence[:i] 未匹配的最小长度
        count_array = [0 for _ in range(len(sentence)+1)]
        for i in range(1, len(sentence)+1):
            count_array[i] = count_array[i-1] + 1
            for word in dictionary:
                if i < len(word):
                    continue
                word_in_sentence = sentence[i-len(word):i]
                if word == word_in_sentence:
                    count_array[i] = min(count_array[i], count_array[i-len(word)])
        return count_array[-1]

