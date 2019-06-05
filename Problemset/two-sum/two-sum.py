
# @Title: 两数之和 (Two Sum)
# @Author: KivenC
# @Date: 2019-06-04 16:16:25
# @Runtime: 76 ms
# @Memory: 14 MB

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        hashmap = dict()
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
