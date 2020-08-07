
# @Title: 课程表 (Course Schedule)
# @Author: KivenC
# @Date: 2020-08-04 09:43:58
# @Runtime: 52 ms
# @Memory: 14.3 MB

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 拓扑排序
        # 考虑排在栈的最底层的元素，是没有任何先决条件的
        # [a, b] 可用有向图表示 a <- b
        # 也就是在栈的最底层， 该元素的入度为 0
        # 将其出栈后，与其相连的元素入度减 1
        # 最后比较出栈次数与总元素个数是否相符
        edges = collections.defaultdict(list)
        indegree = [0] * numCourses
        visited = 0

        for a, b in prerequisites:
            edges[b].append(a)
            indegree[a] += 1
        
        # 将入度为 0 的元素入栈
        stack = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        while stack:
            visited += 1
            v = stack.popleft()
            for n in edges[v]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    stack.append(n)
        
        return visited == numCourses

