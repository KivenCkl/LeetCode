
# @Title: 数组的相对排序 (Relative Sort Array)
# @Author: KivenC
# @Date: 2019-07-18 14:56:57
# @Runtime: 48 ms
# @Memory: 13.1 MB

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 统计 arr1 中的元素，按照 arr2 相对顺序填放，剩下的元素按照升序放置
        import collections
        counter = collections.Counter(arr1)
        res = []
        for a in arr2:
            res.extend([a] * counter[a])
            del counter[a]
        for k in sorted(counter.keys()):
            res.extend([k] * counter[k])
        return res
