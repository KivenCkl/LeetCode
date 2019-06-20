
# @Title: 活字印刷 (Letter Tile Possibilities)
# @Author: KivenC
# @Date: 2019-06-15 12:18:08
# @Runtime: 100 ms
# @Memory: 13 MB

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # 回溯算法
        # 参考 https://leetcode-cn.com/problems/letter-tile-possibilities/solution/hui-su-suan-fa-python-dai-ma-by-liweiwei1419/
        record = dict()
        for tile in tiles:
            record[tile] = record.get(tile, 0) + 1
        
        def dfs(record: dict) -> int:
            res = 0
            for key in record.keys():
                if record[key] == 0:
                    continue
                res += 1
                record[key] -= 1
                res += dfs(record)
                record[key] += 1
            return res
        
        return dfs(record)
