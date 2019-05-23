
# @Title: 组合总和 (Combination Sum)
# @Author: KivenC
# @Date: 2018-07-19 13:51:38
# @Runtime: 84 ms
# @Memory: N/A

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        candidates.sort()
        Solution.res = []
        self.DFS(candidates, target, 0, [])
        return Solution.res
    
    def DFS(self, candidates, target, start, value_list):
        if target == 0:
            return Solution.res.append(value_list)
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, value_list + [candidates[i]])
