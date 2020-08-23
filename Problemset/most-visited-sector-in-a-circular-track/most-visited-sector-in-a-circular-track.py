
# @Title: 圆形赛道上经过次数最多的扇区 (Most Visited Sector in  a Circular Track)
# @Author: KivenC
# @Date: 2020-08-23 10:45:22
# @Runtime: 64 ms
# @Memory: 13.5 MB

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        record = [0] * n
        record[rounds[0]%n] = 1
        for i in range(1, len(rounds)):
            if rounds[i] > rounds[i-1]:
                for k in range(rounds[i-1]+1, rounds[i]+1):
                    record[k % n] += 1
            else:
                tmp = rounds[i] + n
                for k in range(rounds[i-1]+1, tmp+1):
                    record[k % n] += 1
        max_count = max(record)
        res = []
        for i, v in enumerate(record):
            if v == max_count:
                res.append(i)
        if res[0] == 0:
            res = res[1:] + [n]
        return res
