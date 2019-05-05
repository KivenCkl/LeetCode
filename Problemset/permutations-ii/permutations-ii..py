
# @Title: 全排列 II (Permutations II)
# @Author: KivenC
# @Date: 2019-03-01 21:23:41
# @Runtime: 92 ms
# @Memory: 13.3 MB

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i, num in enumerate(nums):
            temp_seq = []
            for li in ans:
                for j in range(i + 1):
                    if j != 0 and num == li[j - 1]: # 关键
                        break
                    temp_li = li[:]
                    temp_li.insert(j, num)
                    temp_seq.append(temp_li)
            ans = temp_seq
        return ans
