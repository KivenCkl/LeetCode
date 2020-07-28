
# @Title: 数组中数字出现的次数 (数组中数字出现的次数 LCOF)
# @Author: KivenC
# @Date: 2020-07-20 19:13:40
# @Runtime: 56 ms
# @Memory: 14.8 MB

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # record = set()
        # for num in nums:
        #     if num in record:
        #         record.remove(num)
        #     else:
        #         record.add(num)
        # return list(record)

        res = functools.reduce(lambda a, b: a ^ b, nums, 0)
        tmp = 1
        while res & tmp == 0:
            tmp <<= 1
        a, b = 0, 0
        for num in nums:
            if num & tmp == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]

