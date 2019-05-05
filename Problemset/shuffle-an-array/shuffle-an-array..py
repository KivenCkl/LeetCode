
# @Title: 打乱数组 (Shuffle an Array)
# @Author: KivenC
# @Date: 2019-03-13 11:54:48
# @Runtime: 732 ms
# @Memory: 19.2 MB

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        return random.sample(self.nums, len(self.nums))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
