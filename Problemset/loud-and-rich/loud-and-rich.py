
# @Title: 喧闹和富有 (Loud and Rich)
# @Author: KivenC
# @Date: 2020-08-05 15:41:39
# @Runtime: 528 ms
# @Memory: 24.1 MB

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # 构建有向图
        # 递归寻找第 i 个最安静的人
        n = len(quiet)
        res = [-1] * n
        graph = [[] for _ in range(n)]
        for x, y in richer:
            graph[y].append(x)
        
        def _loudAndRich(i):
            if res[i] > -1: return res[i]
            res[i] = i
            for j in graph[i]:
                tmp = _loudAndRich(j)
                if quiet[tmp] < quiet[res[i]]:
                    res[i] = tmp
            return res[i]

        return map(_loudAndRich, range(n))

