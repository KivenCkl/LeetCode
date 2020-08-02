
# @Title: 最大得分 (Get the Maximum Score)
# @Author: KivenC
# @Date: 2020-08-02 11:18:04
# @Runtime: 188 ms
# @Memory: 23 MB

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                tmp = max(sum1, sum2)
                sum1 = sum2 = tmp + nums1[i]
                i, j = i + 1, j + 1
        if i < len(nums1):
            sum1 += sum(nums1[i:])
        if j < len(nums2):
            sum2 += sum(nums2[j:])
        return max(sum1, sum2) % (10**9 + 7)

