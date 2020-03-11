
# @Title: 数组中的第K个最大元素 (Kth Largest Element in an Array)
# @Author: KivenC
# @Date: 2019-07-09 14:33:38
# @Runtime: 88 ms
# @Memory: 13.7 MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
#         # way 1
#         import heapq
        
#         return heapq.nlargest(k, nums)[-1]
    
        # way 2
        # 借助快排思想
        tmp = nums[len(nums)//2]
        l, m, r = [], [], []
        for num in nums:
            if num > tmp:
                l.append(num)
            elif num == tmp:
                m.append(num)
            else:
                r.append(num)
        if k <= len(l):
            return self.findKthLargest(l, k)
        elif k <= len(l) + len(m):
            return tmp
        else:
            return self.findKthLargest(r, k-len(l)-len(m))
