
# @Title: 和为目标值的最大数目不重叠非空子数组数目 (Maximum Number of Non-Overlapping Subarrays With Sum Equals Target)
# @Author: KivenC
# @Date: 2020-08-10 21:44:20
# @Runtime: 176 ms
# @Memory: 20.6 MB

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # 前缀和 + 贪心
        record = {0}
        cur_sum, res = 0, 0
        for num in nums:
            cur_sum += num
            if cur_sum - target in record:
                record, cur_sum = {0}, 0
                res += 1
            else:
                record.add(cur_sum)
        return res

