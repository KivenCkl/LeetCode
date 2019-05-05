
# @Title: 到最近的人的最大距离 (Maximize Distance to Closest Person)
# @Author: KivenC
# @Date: 2018-07-18 09:56:00
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        count, res = 0, 0
        for seat in seats:
            if seat == 0:
                count += 1
            else:
                res = max(res, count)
                count = 0
        res = (res + 1) // 2
        count = 0
        if seats[0] == 0:
            for seat in seats:
                if seat == 0:
                    count += 1
                else:
                    break
        res = max(res, count)
        count = 0
        if seats[-1] == 0:
            for seat in seats[::-1]:
                if seat == 0:
                    count += 1
                else:
                    break
        res = max(res, count)
        return res
