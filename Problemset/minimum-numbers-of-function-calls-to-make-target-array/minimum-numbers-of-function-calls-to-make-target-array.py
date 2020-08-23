
# @Title: 得到目标数组的最少函数调用次数 (Minimum Numbers of Function Calls to Make Target Array)
# @Author: KivenC
# @Date: 2020-08-23 00:52:21
# @Runtime: 1616 ms
# @Memory: 18.4 MB

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        while any(nums):
            if all([num % 2 == 0 for num in nums]):
                for i in range(n):
                    nums[i] //= 2
                count += 1
            else:
                for i in range(n):
                    if nums[i] % 2:
                        nums[i] -= 1
                        count += 1
        return count

