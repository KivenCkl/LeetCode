
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: KivenC
# @Date: 2018-07-26 17:18:37
# @Runtime: 100 ms
# @Memory: N/A

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxarea = 0
        while left < right:
            if height[left] < height[right]:
                maxarea = max(maxarea, height[left] * (right - left))
                left += 1
            else:
                maxarea = max(maxarea, height[right] * (right - left))
                right -= 1
        return maxarea
