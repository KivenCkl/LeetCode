
# @Title: 求众数 (Majority Element)
# @Author: KivenC
# @Date: 2019-03-13 10:01:10
# @Runtime: 104 ms
# @Memory: 14.4 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
