
# @Title: 克隆图 (Clone Graph)
# @Author: KivenC
# @Date: 2020-08-12 18:26:17
# @Runtime: 48 ms
# @Memory: 14 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # # bfs
        # if not node:
        #     return
        # visited = {}  # 记录访问过的节点，防止死循环
        # queue = collections.deque([node])
        # visited[node] = Node(node.val)
        # while queue:
        #     n = queue.popleft()
        #     for neighbor in n.neighbors:
        #         if neighbor not in visited:
        #             visited[neighbor] = Node(neighbor.val)
        #             queue.append(neighbor)
                    
        #         visited[n].neighbors.append(visited[neighbor])  # 更新节点
                    
        # return visited[node]

        # dfs
        if not node:
            return 
        visited = {}

        def dfs(origin):
            if origin not in visited:
                visited[origin] = node = Node(origin.val)
                node.neighbors += [dfs(n) for n in origin.neighbors]
            return visited[origin]
        
        return dfs(node)

