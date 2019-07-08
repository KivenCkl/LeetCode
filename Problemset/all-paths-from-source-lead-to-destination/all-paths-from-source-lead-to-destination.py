
# @Title: 从始点到终点的所有路径 (All Paths from Source Lead to Destination)
# @Author: KivenC
# @Date: 2019-04-18 11:14:34
# @Runtime: 160 ms
# @Memory: 16.1 MB

from collections import defaultdict
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(set)
        for edge in edges:
            dic[edge[0]].add(edge[1])
        if destination in dic:
            return False
        if n == 1:
            return True
        return self.possiblepath(source, destination, dic, set([source]))
    
    def possiblepath(self, source, destination, dic, path):
        if source not in dic or destination in dic:
            return False
        for ne in dic[source]:
            if ne in path:
                return False
            elif ne == destination:
                continue
            else:
                path.add(ne)
                if not self.possiblepath(ne, destination, dic, path):
                    return False
                path.remove(ne)
        return True
