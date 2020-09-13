
# @Title: 统计不开心的朋友 (Count Unhappy Friends)
# @Author: KivenC
# @Date: 2020-09-13 12:27:54
# @Runtime: 176 ms
# @Memory: 32.1 MB

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        records = [{p: i for i, p in enumerate(preference[::-1])} for preference in preferences]
        unhappy = set()

        def helper(a, b):
            if records[a[0]][a[1]] < records[a[0]][b[0]] and records[b[0]][b[1]] < records[b[0]][a[0]]:
                unhappy.add(a[0])
                unhappy.add(b[0])
            
        for i in range(len(pairs)):
            for j in range(i+1, len(pairs)):
                helper(pairs[i], pairs[j])
                helper(pairs[i][::-1], pairs[j])
                helper(pairs[i], pairs[j][::-1])
                helper(pairs[i][::-1], pairs[j][::-1])
        return len(unhappy)

