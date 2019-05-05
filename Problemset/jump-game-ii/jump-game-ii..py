
# @Title: 跳跃游戏 II (Jump Game II)
# @Author: KivenC
# @Date: 2019-03-01 09:07:22
# @Runtime: 80 ms
# @Memory: 14.5 MB

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        i, step, jump_point, max_dis = 0, 0, 0, nums[0]
        while i < len(nums):
            step += 1
            if max_dis >= len(nums) - 1:
                return step
            for j in range(i+1, i+nums[i]+1):
                temp = j + nums[j]
                if temp >= len(nums) - 1:
                    return step + 1
                if temp > max_dis:
                    max_dis = temp
                    jump_point = j
            i = jump_point
