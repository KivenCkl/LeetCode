
# @Title: 等价多米诺骨牌对的数量 (Number of Equivalent Domino Pairs)
# @Author: KivenC
# @Date: 2019-07-31 21:20:36
# @Runtime: 336 ms
# @Memory: 23.5 MB

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         # way 1
#         # 以元组为键
#         ans = 0
#         counter = {}
#         for domino in dominoes:
            
#             if domino[0] > domino[1]:
#                 domino[0], domino[1] = domino[1], domino[0]
            
#             key = (domino[0], domino[1])
#             val = counter.get(key, 0)
#             ans += val  # 原来 key 出现了几次，那么新加入 1 个 key 就能新组成几个匹配对
#             counter[key] = val + 1
#         return ans
        
#         # way 2
#         # 将 domino 拼成一个数作为键
#         import collections
#         counter, ans = collections.defaultdict(int), 0
#         for i, j in dominoes:
#             key = 10 * i + j if i < j else 10 * j + i
#             ans += counter[key]
#             counter[key] += 1
#         return ans

        # way 3
        # 不用字典，使用列表进行记录
        ans = 0
        record = [[0 for _ in range(10)] for _ in range(10)]
        for i, j in dominoes:
            if i > j:
                i, j = j, i
            ans += record[i][j]
            record[i][j] += 1
        return ans
