
# @Title: 魔术索引 (Magic Index LCCI)
# @Author: KivenC
# @Date: 2020-07-31 10:11:27
# @Runtime: 36 ms
# @Memory: 14.5 MB

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        if nums[0] == 0: return 0
        m, n = 0, len(nums)
        while m < n:
            if nums[m] < m: m += 1
            elif nums[m] == m: return m
            else: m = nums[m]
        return -1

