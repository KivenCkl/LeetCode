
# @Title: 早餐组合 (早餐组合)
# @Author: KivenC
# @Date: 2020-09-12 15:46:02
# @Runtime: 516 ms
# @Memory: 30.2 MB

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        res = collections.Counter(filter(lambda x: x >= 0, [x - a for a in staple]))
        drinks.sort()
        count = 0
        n = len(drinks)
        for k, v in res.items():
            mid = bisect.bisect_right(drinks, k)
            count += v * mid
        return count % 1000000007
