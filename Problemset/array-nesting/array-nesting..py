
# @Title: 数组嵌套 (Array Nesting)
# @Author: KivenC
# @Date: 2018-08-05 22:09:31
# @Runtime: 144 ms
# @Memory: N/A

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [False] * len(nums)
        ans = 0
        for i in range(len(nums)):
            count = 0
            while not visited[i]:
                count += 1
                visited[i] = True
                i = nums[i]
            ans = max(ans, count)
        return ans
