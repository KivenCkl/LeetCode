
# @Title: 两个数组的交集 II (Intersection of Two Arrays II)
# @Author: KivenC
# @Date: 2020-07-13 09:59:15
# @Runtime: 56 ms
# @Memory: 13.7 MB

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        return (counter1 & counter2).elements()
