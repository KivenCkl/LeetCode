
# @Title: 组合 (Combinations)
# @Author: KivenC
# @Date: 2020-09-08 22:00:15
# @Runtime: 56 ms
# @Memory: 15.1 MB

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # res = []
        # nums = list(range(1, n + 1))

        # def helper(nums, path):
        #     if len(path) == k:
        #         res.append(path)
        #     if not nums:
        #         return
        #     for i, num in enumerate(nums):
        #         helper(nums[i+1:], path + [num])
        
        # helper(nums, [])
        # return res

        # return list(itertools.combinations(range(1,n + 1),k))

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

