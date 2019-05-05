
# @Title: 最短无序连续子数组 (Shortest Unsorted Continuous Subarray)
# @Author: KivenC
# @Date: 2018-07-17 16:11:42
# @Runtime: 128 ms
# @Memory: N/A

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index, right_index = 0, len(nums)-1
        # 为了保证当该数组原本就是升序时返回0
        i, j = 0, -1
        min_num, max_num = nums[-1], nums[0]
        while(right_index >= 0):
            max_num = max(max_num, nums[left_index])
            # 记录不符合升序规则的最大索引
            if nums[left_index] != max_num:
                j = left_index
            left_index += 1
            min_num = min(min_num, nums[right_index])
            # 记录不符合规则的最小索引
            if nums[right_index] != min_num:
                i = right_index
            right_index -= 1
        return j - i + 1
