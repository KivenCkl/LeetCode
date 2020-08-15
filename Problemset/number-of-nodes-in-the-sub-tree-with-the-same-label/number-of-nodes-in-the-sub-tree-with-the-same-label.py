
# @Title: 子树中标签相同的节点数 (Number of Nodes in the Sub-Tree With the Same Label)
# @Author: KivenC
# @Date: 2020-08-11 19:16:11
# @Runtime: 464 ms
# @Memory: 157.2 MB

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # # 用全局 visited 集合变量记录
        # res = [0 for _ in range(n)]
        # record = collections.defaultdict(list)
        # for x, y in edges:
        #     record[x].append(y)
        #     record[y].append(x)
        
        # def _dfs(i):
        #     data = collections.Counter(labels[i])
        #     visited.add(i)
        #     for j in record[i]:
        #         if j in visited:
        #             continue
        #         data += _dfs(j)
        #     res[i] += data.get(labels[i])
        #     return data
        
        # visited = set()
        # _dfs(0)
        # return res

        # 用 pre 变量记录
        record = [[] for _ in range(n)]
        for a, b in edges:
            record[a].append(b)
            record[b].append(a)
        
        res = [0] * n
        cnt = collections.defaultdict(int)
        def dfs(x, pre):
            cur_cnt = cnt[labels[x]]
            for y in record[x]:
                if y == pre: continue
                dfs(y, x)
            cnt[labels[x]] += 1
            res[x] = cnt[labels[x]] - cur_cnt
            
        dfs(0, -1)
        return res

