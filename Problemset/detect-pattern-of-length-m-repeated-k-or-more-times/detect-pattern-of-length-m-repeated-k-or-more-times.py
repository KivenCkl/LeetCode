
# @Title: 重复至少 K 次且长度为 M 的模式 (Detect Pattern of Length M Repeated K or More Times)
# @Author: KivenC
# @Date: 2020-08-30 10:42:46
# @Runtime: 36 ms
# @Memory: 13.8 MB

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i = 0
        tmp = i
        j = k
        n = len(arr)
        if n < m * k:
            return False
        while i < n - m + 1:
            if j < 2:
                return True
            pattern = arr[i:i+m]
            if arr[i+m:i+2*m] == pattern:
                j -= 1
                i += m
            else:
                i = tmp + 1
                tmp = i
                j = k
        return False
            
