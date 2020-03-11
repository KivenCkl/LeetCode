
# @Title: 划分为k个相等的子集 (Partition to K Equal Sum Subsets)
# @Author: KivenC
# @Date: 2019-10-20 18:33:46
# @Runtime: 52 ms
# @Memory: 13.9 MB

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 回溯
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        n = len(nums)
        visited = set()
        
        def dfs(k, tmp_sum, loc):
            if tmp_sum == target:
                return dfs(k-1, 0, 0)
            if k == 1:
                return True
            for i in range(loc, n):
                if i not in visited and nums[i] + tmp_sum <= target:
                    visited.add(i)
                    if dfs(k, tmp_sum + nums[i], i + 1):
                        return True
                    visited.remove(i)
            return False
        return dfs(k, 0, 0)
