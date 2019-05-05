
# @Title: 全排列 (Permutations)
# @Author: KivenC
# @Date: 2019-03-01 21:14:43
# @Runtime: 68 ms
# @Memory: 13.2 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i, num in enumerate(nums):
            temp_seq = []
            for li in ans:
                for j in range(i+1):
                    temp_li = li[:]
                    temp_li.insert(j, num)
                    temp_seq.append(temp_li)
            ans = temp_seq
        return ans
