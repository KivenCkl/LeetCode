
# @Title: 两个数组的交集 II (Intersection of Two Arrays II)
# @Author: KivenC
# @Date: 2019-03-13 13:18:32
# @Runtime: 60 ms
# @Memory: 13.2 MB

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        ans = []
        len_1, len_2 = len(nums1), len(nums2)
        if len_1 < len_2:
            for num in nums1:
                if num in nums2:
                    ans.append(num)
                    nums2.remove(num)
        else:
            for num in nums2:
                if num in nums1:
                    ans.append(num)
                    nums1.remove(num)
        return ans
        '''
        counter = {}
        ans = []
        for num in nums1:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for num in nums2:
            if num in counter and counter[num] > 0:
                ans.append(num)
                counter[num] -= 1
        return ans
