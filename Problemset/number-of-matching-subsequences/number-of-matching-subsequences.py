
# @Title: 匹配子序列的单词数 (Number of Matching Subsequences)
# @Author: KivenC
# @Date: 2018-07-20 20:04:51
# @Runtime: 1432 ms
# @Memory: N/A

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # way 1
        # subsets = [[]]
        # for s in S:
        #     subsets += [subset + [s] for subset in subsets]
        # count = 0
        # for word in words:
        #     if list(word) in subsets:
        #         count += 1
        # return count
        
        # way 2
        count = 0
        dic = collections.defaultdict(list)
        for word in words:
            dic[word[0]].append(word)
        for char in S:
            queue = dic[char]
            for _ in range(len(queue)):
                word = queue.pop(0)
                if len(word) == 1:
                    count += 1
                elif len(word) > 1:
                    word = word[1:]
                    dic[word[0]].append(word)
        return count
