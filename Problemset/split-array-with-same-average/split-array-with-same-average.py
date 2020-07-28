
# @Title: 数组的均值分割 (Split Array With Same Average)
# @Author: KivenC
# @Date: 2020-07-10 19:16:51
# @Runtime: 60 ms
# @Memory: 13.7 MB

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        # sum(A) / len(A) = sum(A1) / len(A1) = sum(A - A1) / len(A - A1)
        A.sort()
        n = len(A)
        s = sum(A)
        for i in range(1, n//2+1):
            if s * i % n == 0 and self.dfs(A, 0, i, s*i//n):
                return True
        return False
    
    def dfs(self, A: List[int], begin: int, k: int, target: int) -> bool:
        # 寻找有序数组 A[begin:] 中 k 个数累加为 target
        if k == 0:
            return target == 0
        if target < k * A[begin]:
            return False
        for i in range(begin, len(A)-k+1):
            if i > begin and A[i] == A[i-1]:
                continue
            if self.dfs(A, i+1, k-1, target-A[i]):
                return True
        return False
