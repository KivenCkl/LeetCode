
# @Title: 存在重复元素 II (Contains Duplicate II)
# @Author: KivenC
# @Date: 2018-07-17 13:34:37
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2 or k <= 0:
            return False
        record = set([])
        for i in range(len(nums)):
            if i > k:
                # 集合的discard()函数：判断某元素是否存在于该集合，如果存在则删除
                record.discard(nums[i-k-1])
            if nums[i] in record:
                return True
            record.add(nums[i])
        return False
