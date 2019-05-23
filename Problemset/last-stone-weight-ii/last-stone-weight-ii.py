
# @Title: 最后一块石头的重量 II (Last Stone Weight II)
# @Author: KivenC
# @Date: 2019-05-23 00:45:35
# @Runtime: 60 ms
# @Memory: 13.2 MB

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
#         # way 1
#         # 每一块石头要么加要么减，记录添加每一块石头会得到的结果，最后返回最小值
#         res = {0}
#         half_sum_weight = sum(stones) / 2
        
#         for stone in stones:
#             new_res = set()
            
#             while res:
#                 s = res.pop()
#                 # 剪枝
#                 if s + stone <= half_sum_weight:
#                     new_res.add(s + stone)
#                 if s - stone >= -half_sum_weight:
#                     new_res.add(s - stone)
                    
#             res = new_res
#         return min(map(abs, res))

#         # way 2
#         # 将这堆石头分成两堆，最终结果就是这两堆石头重量和的最小差值
        dp = {0}  # 记录其中一堆所有可能的重量和
        sum_weight = 0
        for stone in stones:
            sum_weight += stone
            dp |= {stone + i for i in dp}
        res = float('inf')
        for iv in dp:
            res = min(res, abs(sum_weight - 2 * iv))  # 求最小差值
        
        return res
