
# @Title: 复写零 (Duplicate Zeros)
# @Author: KivenC
# @Date: 2019-07-01 21:05:00
# @Runtime: 80 ms
# @Memory: 13.1 MB

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
#         # way 1
#         # O(n^2)
#         i = 0
        
#         while i < len(arr) - 1:
#             if arr[i] == 0:
#                 arr[i+2:] = arr[i+1:-1]
#                 arr[i+1] = 0
#                 i += 2
#             else:
#                 i += 1

        # way 2
        # 借用数组副本辅助记录
        cop = arr[:]
        n = len(arr)
        i, j = 0, 0
        while j < n:
            arr[j] = cop[i]
            if cop[i] == 0:
                j += 1
                if j < n:
                    arr[j] = 0
            j += 1
            i += 1
