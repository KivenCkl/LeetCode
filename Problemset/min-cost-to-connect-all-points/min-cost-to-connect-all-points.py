
# @Title: 连接所有点的最小费用 (Min Cost to Connect All Points)
# @Author: KivenC
# @Date: 2020-09-13 12:43:59
# @Runtime: 3588 ms
# @Memory: 66.4 MB

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # n = len(points)
        # if n < 2:
        #     return 0

        # cost_list = []
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         x1, y1 = points[i]
        #         x2, y2 = points[j]
        #         cost = abs(x1 - x2) + abs(y1 - y2)
        #         cost_list.append((cost, i, j))
        # cost_list.sort(key=lambda x: x[0])

        # res = 0
        # nodes = [i for i in range(n)]

        # def getRoot(x):
        #     if nodes[x] == x:
        #         return x
        #     else:
        #         return getRoot(nodes[x])

        # for cost, i, j in cost_list:
        #     root_i = getRoot(i)
        #     root_j = getRoot(j)
        #     if root_i != root_j:
        #         nodes[root_i] = root_j
        #         res += cost

        # return res

        cal = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # 计算曼哈顿距离
        import queue
        pq = queue.PriorityQueue()  # 优先队列
        visited = set([i for i in range(len(points))])
        res = 0

        pq.put((0, 0))  # (distance, point_id)
        while visited: 
            dis, now = pq.get()  # (到扩展集中某最近点的距离，某最近点的序号)
            if now not in visited:  # 已访问过的直接跳过
                continue
            visited.remove(now)  # 剪枝
            res += dis
            for i in visited:
                pq.put((cal(points[now], points[i]), i))  # 按距离丢进优先队列排序

        return res

