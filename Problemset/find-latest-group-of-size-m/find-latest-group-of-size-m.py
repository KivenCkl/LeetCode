
# @Title: 查找大小为 M 的最新分组 (Find Latest Group of Size M)
# @Author: KivenC
# @Date: 2020-08-23 13:53:05
# @Runtime: 6392 ms
# @Memory: 24.4 MB

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        start = [0, n + 1]
        for i, t in enumerate(arr[::-1]) :
            idt = bisect.bisect(start, t)
            start.insert(idt, t)
            if m == start[idt+1]-start[idt]-1 or m == start[idt]-start[idt-1]-1:
                return len(arr)-i-1
        return -1

