
# @Title: 合并两个有序数组 (Merge Sorted Array)
# @Author: KivenC
# @Date: 2019-03-02 11:04:57
# @Runtime: 76 ms
# @Memory: 13.3 MB

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[end] = nums2[n - 1]
                n -= 1
            else:
                nums1[end] = nums1[m - 1]
                m -= 1
            end -= 1
        while n > 0:
            nums1[end] = nums2[n - 1]
            n -= 1
            end -= 1
