
# @Title: 第 k 个缺失的正整数 (Kth Missing Positive Number)
# @Author: KivenC
# @Date: 2020-08-08 22:53:52
# @Runtime: 48 ms
# @Memory: 13.7 MB

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        j = 1
        while k > 0 and i < len(arr):
            if arr[i] != j:
                k -= 1
            else:
                i += 1
            j += 1
        if k > 0:
            j += k
        return j - 1
                
                
