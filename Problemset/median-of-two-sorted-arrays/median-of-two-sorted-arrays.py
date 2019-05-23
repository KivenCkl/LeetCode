
# @Title: 寻找两个有序数组的中位数 (Median of Two Sorted Arrays)
# @Author: KivenC
# @Date: 2018-10-25 11:05:43
# @Runtime: 164 ms
# @Memory: N/A

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 归并排序
        new_list = list()
        a = b = 0
        m, n = len(nums1), len(nums2)
        while a < m and b < n:
            if nums1[a] <= nums2[b]:
                new_list.append(nums1[a])
                a += 1
            else:
                new_list.append(nums2[b])
                b += 1
        while a < m:
            new_list.append(nums1[a])
            a += 1
        while b < n:
            new_list.append(nums2[b])
            b += 1
        if (m + n) % 2:
            return new_list[(m+n)//2] / 1.0 
        else:
            return (new_list[(m+n)//2] + new_list[(m+n)//2-1]) / 2.0
