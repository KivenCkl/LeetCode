
# @Title: 接雨水 (Trapping Rain Water)
# @Author: KivenC
# @Date: 2019-02-25 14:24:28
# @Runtime: 52 ms
# @Memory: 7 MB

class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        
        if len(height) > 2:

            max_value = max(height)
            value_index = height.index(max_value)

            v = 0

            for i in range(1,value_index):
                if height[i] >= height[0]:
                    height[0] = height[i]
                else:
                    v=v+height[0]-height[i]

            for i in range(2,len(height)-value_index):
                if height[-i] >= height[-1]:
                    height[-1] = height[-i]
                else:
                    v=v+height[-1]-height[-i]

            return v


        else:
            return 0
