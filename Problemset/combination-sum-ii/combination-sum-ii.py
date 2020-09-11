
# @Title: 组合总和 II (Combination Sum II)
# @Author: KivenC
# @Date: 2020-09-10 22:16:31
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def helper(start, n, target, path):
            if target == 0:
                res.append(path)
            for i in range(start, n):
                if target < candidates[i]:
                    return
                if i != start and candidates[i] == candidates[i-1]:
                    continue
                helper(i + 1, n, target - candidates[i], path + [candidates[i]])
        
        helper(0, n, target, [])
        return res

