
# @Title: 组合总和 (Combination Sum)
# @Author: KivenC
# @Date: 2020-09-09 20:10:07
# @Runtime: 48 ms
# @Memory: 13.7 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def helper(start, target, path):
            if target == 0:
                res.append(path)
            for i in range(start, n):
                if target < candidates[i]:
                    return
                helper(i, target - candidates[i], path + [candidates[i]])

        helper(0, target, [])
        return res

