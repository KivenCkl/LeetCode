
# @Title: 四数相加 II (4Sum II)
# @Author: KivenC
# @Date: 2019-03-26 18:56:20
# @Runtime: 228 ms
# @Memory: 34 MB

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # record, ans = dict(), 0
        # for a in A:
        #     for b in B:
        #         record[a+b] = record.get(a+b, 0) + 1
        # for c in C:
        #     for d in D:
        #         ans += record.get(-(c+d), 0)
        # return ans
        from collections import Counter
        AA, BB, CC, DD = map(Counter, (A, B, C, D))
        dic, ans = {}, 0
        for a_i, a_v in AA.items():
            for b_i, b_v in BB.items():
                dic[a_i + b_i] = dic.get(a_i + b_i, 0) + a_v * b_v
        for c_i, c_v in CC.items():
            for d_i, d_v in DD.items():
                if -(c_i + d_i) in dic:
                    ans += dic.get(-(c_i + d_i)) * c_v * d_v
        return ans
