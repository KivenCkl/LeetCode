
# @Title: 存在重复元素 (Contains Duplicate)
# @Author: KivenC
# @Date: 2019-03-13 11:27:31
# @Runtime: 100 ms
# @Memory: 18.7 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
