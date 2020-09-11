
# @Title: 前 K 个高频元素 (Top K Frequent Elements)
# @Author: KivenC
# @Date: 2020-09-07 22:37:32
# @Runtime: 64 ms
# @Memory: 16.5 MB

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in collections.Counter(nums).most_common(k)]

