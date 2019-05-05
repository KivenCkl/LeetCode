
# @Title: 组合总和 II (Combination Sum II)
# @Author: KivenC
# @Date: 2018-07-24 19:37:45
# @Runtime: 68 ms
# @Memory: N/A

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        self.DFS(candidates, target, 0, [])
        return self.res
    
    def DFS(self, candidates, target, start, value_list):
        if target == 0:
            return self.res.append(value_list)
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            if i != start and candidates[i-1] == candidates[i]:
                continue
            self.DFS(candidates, target - candidates[i], i + 1, value_list + [candidates[i]])
