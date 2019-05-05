
# @Title: 较大分组的位置 (Positions of Large Groups)
# @Author: KivenC
# @Date: 2018-07-15 19:19:41
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res, count, first_index = [], 1, 0
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
                if i == len(S) - 1:
                    res.append([first_index, i])
            else:
                res.append([first_index, first_index + count - 1])
                first_index = i
                count = 1
        return [r for r in res if r[1] - r[0] > 1]
