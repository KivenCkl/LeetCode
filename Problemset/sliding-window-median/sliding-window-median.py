
# @Title: 滑动窗口中位数 (Sliding Window Median)
# @Author: KivenC
# @Date: 2019-10-28 18:27:06
# @Runtime: 196 ms
# @Memory: 15.6 MB

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        temp = sorted(nums[:k])
        res.append((temp[(k - 1) // 2] + temp[k // 2]) / 2)
        for i in range(k, len(nums)):
            index = self.erfen(temp, nums[i - k])
            temp.pop(index)
            pos = self.erfen(temp, nums[i])
            temp.insert(pos, nums[i])
            res.append((temp[(k - 1) // 2] + temp[k // 2]) / 2)
        return res
        
    
    def erfen(self, nums: List[int], num: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == num:
                return mid
            elif nums[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return left

