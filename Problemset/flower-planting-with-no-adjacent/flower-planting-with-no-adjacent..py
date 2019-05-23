
# @Title: 不邻接植花 (Flower Planting With No Adjacent)
# @Author: KivenC
# @Date: 2019-05-18 23:01:07
# @Runtime: 224 ms
# @Memory: 17.8 MB

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
#         way 1
#         # 将所有路径转换为 dict，key 为花园序号，value 为可到达的花园序号
#         import collections
#         path_dic = collections.defaultdict(list)
#         for path in paths:
#             path_dic[path[0]].append(path[1])
#             path_dic[path[1]].append(path[0])
    
#         # 对于每个花园，如果它能到达的花园已经种了花，那么就排除这种花的可能
#         # 对第一个花园而言，其可以到达的花园都没有种花，因此可以选择种第一种花
#         res = [1]
#         for i in range(1, N):  # i 代表第 i + 1 个花园
#             flowers = [1, 2, 3, 4]
#             for p in path_dic[i + 1]:
#                 if p > len(res) or res[p-1] not in flowers:
#                     continue
#                 flowers.remove(res[p-1])
#             res.append(flowers[0])
#         return res
#
#         way 2
        guards = [[] for _ in range(N+1)]
        # 创建邻接矩阵
        for path in paths:
            guards[path[0]].append(path[1])
            guards[path[1]].append(path[0])
        
        res = [0] * (N + 1)
        for i in range(1, N + 1):
            tmp = 1
            flowers = set()
            # 获取邻居中的所有 flowers
            for n in guards[i]:
                flower = res[n]
                if flower != 0 and flower not in flowers:
                    flowers.add(flower)
            # 决定自己的 flower
            while tmp in flowers:
                tmp += 1
            
            res[i] = tmp
        return res[1:]
