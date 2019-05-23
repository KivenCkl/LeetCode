
# @Title: 和为K的子数组 (Subarray Sum Equals K)
# @Author: KivenC
# @Date: 2018-07-19 18:00:52
# @Runtime: 84 ms
# @Memory: N/A

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # key为前n项的和，value为该和出现的次数
        sum_dic = {0: 1}
        temp, count = 0, 0
        for num in nums:
            temp += num
            # 寻找key为temp-k的值
            count += sum_dic.get(temp-k, 0)
            # 每出现一次和为temp，则该value加一
            sum_dic[temp] = sum_dic.get(temp, 0) + 1
        return count
