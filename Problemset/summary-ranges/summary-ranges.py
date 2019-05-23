
# @Title: 汇总区间 (Summary Ranges)
# @Author: KivenC
# @Date: 2018-07-25 17:47:11
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return []
        res = []
        start = nums[0]
        nums.append(sys.maxsize)
        count = 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                if count > 0:
                    res.append("%s->%s" % (start, start+count))
                elif count == 0:
                    res.append("%s" % start)
                start = nums[i+1]
                count = 0
        return res
