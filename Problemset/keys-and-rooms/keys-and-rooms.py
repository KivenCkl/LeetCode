
# @Title: 钥匙和房间 (Keys and Rooms)
# @Author: KivenC
# @Date: 2020-08-31 22:42:46
# @Runtime: 80 ms
# @Memory: 14 MB

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [0]
        while stack:
            key = stack.pop()
            for k in rooms[key]:
                if not visited[k]:
                    visited[k] = True
                    stack.append(k)
        return all(visited)

