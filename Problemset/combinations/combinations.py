
# @Title: 组合 (Combinations)
# @Author: KivenC
# @Date: 2019-05-08 15:39:31
# @Runtime: 232 ms
# @Memory: 14.8 MB

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # way 1
        # import itertools
        # return list(itertools.combinations(range(1,n + 1),k))
        #
        # way 2
        # 回溯法
        # def dfs(nums, k):
        #     if k == 0:
        #         return []
        #     if k == 1:
        #         return [[i] for i in nums]
        #     res = []
        #     for i, num in enumerate(nums):
        #         for j in dfs(nums[i + 1:], k - 1):
        #             res.append([num] + j)
        #     return res
        # return dfs(list(range(1, n + 1)), k)
        #
        # way 3
        # C(m, n) = C(m-1, n-1) + C(m-1, n)
        # C(5, 3) = C(4, 2) + C(4, 3)
        #         = C(3, 1) + C(3, 2) + C(3, 2) + C(3, 3)
        #         = C(3, 1) + C(2, 1) + C(2, 2) + C(2, 1) + C(2, 2) + C(3, 3)
        if k == 0 or k > n:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]
        ans = self.combine(n - 1, k)  # C(m-1, n)
        for item in self.combine(n - 1, k - 1):  # C(m-1, n-1)
            item.append(n)
            ans.append(item)
        return ans
        
