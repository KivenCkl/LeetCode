
# @Title: 字母异位词分组 (Group Anagrams)
# @Author: KivenC
# @Date: 2019-05-07 20:49:15
# @Runtime: 188 ms
# @Memory: 15.8 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        import functools
        # way 1
        # 记录每个字符串的字母组成，O(NKlogK)
        # res = collections.defaultdict(list)
        # for s in strs:
        #     res[tuple(sorted(s))].append(s)
        # return list(res.values())
        #
        # way 2
        # 记录每个字符串的字母个数，O(NK)
        # res = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)
        # return list(res.values())
        #
        # way 3
        # 用质数表示每个字母，将字符串的各个字母相乘
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        res = collections.defaultdict(list)
        for s in strs:
            res[functools.reduce(lambda x, y: x * y, map(lambda x: prime[ord(x) - ord('a')], s), 1)].append(s)
        return list(res.values())
