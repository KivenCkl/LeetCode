
# @Title: 提莫攻击 (Teemo Attacking)
# @Author: KivenC
# @Date: 2018-07-24 13:50:50
# @Runtime: 116 ms
# @Memory: N/A

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        count = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration <= timeSeries[i+1]:
                count += duration
            else:
                count += timeSeries[i+1] - timeSeries[i]
        return count + duration
