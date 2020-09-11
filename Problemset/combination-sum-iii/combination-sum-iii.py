
# @Title: 组合总和 III (Combination Sum III)
# @Author: KivenC
# @Date: 2020-09-11 21:50:51
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def helper(start, target, path):
            if len(path) == k and target == 0:
                res.append(path)
            if len(path) > k:
                return
            for i in range(start, 10):
                if target < i:
                    return
                helper(i+1, target-i, path+[i])
        
        helper(1, n, [])
        return res

