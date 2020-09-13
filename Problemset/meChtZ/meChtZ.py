
# @Title: 快速公交 (快速公交)
# @Author: KivenC
# @Date: 2020-09-13 13:17:50
# @Runtime: 180 ms
# @Memory: 15.3 MB

class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:

        @functools.lru_cache(None)
        def helper(target):
            if target == 0:
                return 0
            if target == 1:
                return inc
            res = target * inc
            for j, c in zip(jump, cost):
                res = min(res, helper(target // j) + c + (target % j) * inc)
                if target % j > 0:
                    res = min(res, helper(target // j + 1) + c + (j - target % j) * dec)
            return res

        return helper(target) % (10 ** 9 + 7)

