
# @Title: 合并区间 (Merge Intervals)
# @Author: KivenC
# @Date: 2018-07-28 22:18:58
# @Runtime: 100 ms
# @Memory: N/A

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or interval.start > result[-1].end:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result
