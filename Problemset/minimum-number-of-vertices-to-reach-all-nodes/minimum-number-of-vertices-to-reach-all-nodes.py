
# @Title: 可以到达所有点的最少点数目 (Minimum Number of Vertices to Reach All Nodes)
# @Author: KivenC
# @Date: 2020-08-23 00:56:29
# @Runtime: 156 ms
# @Memory: 34.9 MB

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        record_in = set()
        for _, j in edges:
            record_in.add(j)
        return list(filter(lambda x: x not in record_in, range(n)))

