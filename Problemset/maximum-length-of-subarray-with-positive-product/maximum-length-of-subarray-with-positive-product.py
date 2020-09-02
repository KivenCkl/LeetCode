
# @Title: 乘积为正数的最长子数组长度 (Maximum Length of Subarray With Positive Product)
# @Author: KivenC
# @Date: 2020-08-30 14:38:46
# @Runtime: 220 ms
# @Memory: 25 MB

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        pos, neg = 0, 0
        for num in nums:
            if num == 0:
                pos, neg = 0, 0
            elif num > 0:
                pos += 1
                if neg > 0:
                    neg += 1
            else:
                pos, neg = neg + 1 if neg else 0, pos + 1 if pos else 1
            res = max(res, pos)
        return res
                
