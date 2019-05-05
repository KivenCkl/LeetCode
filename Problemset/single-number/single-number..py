
# @Title: 只出现一次的数字 (Single Number)
# @Author: KivenC
# @Date: 2019-03-01 22:19:00
# @Runtime: 88 ms
# @Memory: 14.7 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for num in nums:
            temp ^= num
        return temp
