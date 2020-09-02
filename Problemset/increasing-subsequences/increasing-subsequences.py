
# @Title: 递增子序列 (Increasing Subsequences)
# @Author: KivenC
# @Date: 2020-08-25 23:53:09
# @Runtime: 56 ms
# @Memory: 23.2 MB

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 动态规划
        if not nums:
            return []
        res = {(nums[0], )}
        for i in nums[1:]:
            res.update({j+(i, ) for j in res if j[-1] <= i})
            res.add((i, ))
        return [list(i) for i in res if len(i) > 1]

        # # dfs
        # res = []

        # def dfs(nums: List[int], tmp: List[int]) -> None:
        #     if len(tmp) > 1:
        #         res.append(tmp)
        #     cur = set()
        #     for i, num in enumerate(nums):
        #         if num in cur:
        #             continue
        #         if not tmp or num >= tmp[-1]:
        #             cur.add(num)
        #             dfs(nums[i+1:], tmp+[num])
            
        # dfs(nums, [])
        # return res

