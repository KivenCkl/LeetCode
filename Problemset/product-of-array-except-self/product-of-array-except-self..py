
# @Title: 除自身以外数组的乘积 (Product of Array Except Self)
# @Author: KivenC
# @Date: 2019-03-14 16:13:57
# @Runtime: 236 ms
# @Memory: 20.7 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        from functools import reduce
        return [reduce(lambda x, y: x * y, nums[:i] + nums[i+1:]) for i in range(len(nums))]
        '''
        n = len(nums)
        ans = [1 for _ in range(n)]
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        tmp = 1
        for i in range(n-1, -1, -1):
            ans[i] *= tmp
            tmp *= nums[i]
        return ans
