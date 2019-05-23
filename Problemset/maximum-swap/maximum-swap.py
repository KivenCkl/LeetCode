
# @Title: 最大交换 (Maximum Swap)
# @Author: KivenC
# @Date: 2018-07-23 21:13:53
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = map(int, str(num))
        for i in range(len(nums)-1):
            temp = nums[i:]
            if temp[0] != max(temp):
                max_index = len(temp) - 1 - temp[::-1].index(max(temp))
                nums[i], nums[max_index+i] = nums[max_index+i], nums[i]
                break
        return int(''.join(map(str, nums)))

