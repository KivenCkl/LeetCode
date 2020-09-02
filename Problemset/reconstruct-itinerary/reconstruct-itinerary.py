
# @Title: 重新安排行程 (Reconstruct Itinerary)
# @Author: KivenC
# @Date: 2020-08-27 21:53:33
# @Runtime: 44 ms
# @Memory: 13.9 MB

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # # 回溯
        # record = collections.defaultdict(list)
        # for start, end in tickets:
        #     record[start].append(end)
        
        # for k in record:
        #     record[k].sort()

        # path = ["JFK"]
        # n = len(tickets)

        # def backtrack(start):
        #     if len(path) == n + 1:
        #         return True
        #     for _ in record[start]:
        #         next = record[start].pop(0)
        #         path.append(next)
        #         if backtrack(next):
        #             return True
        #         path.pop()
        #         record[start].append(next)
        #     return False
        
        # backtrack("JFK")
        # return path

        res = []
        paths = collections.defaultdict(list)
        tickets.sort(key=lambda x: x[1], reverse = True)
        for s, t in tickets:
            paths[s].append(t)

        self.dfs('JFK', paths, res)
        return res[::-1]
    
    def dfs(self, dep: str, paths: defaultdict, res: List[str]):
        arr = paths[dep]
        while arr:
            self.dfs(arr.pop(), paths, res)
        res.append(dep)  
            
