
# @Title: 缺失的第一个正数 (First Missing Positive)
# @Author: KivenC
# @Date: 2019-02-25 12:45:35
# @Runtime: 48 ms
# @Memory: 6.5 MB

class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        l = len(nums)
        x = 0
        for i in nums:
            if 0 < i <= l and not x & (1 << (i - 1)):
                x += 1 << (i - 1)
        for i in range(l + 1):
            if not x & 1:
                return i + 1
            x >>= 1
