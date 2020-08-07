
# @Title: 统计好三元组 (Count Good Triplets)
# @Author: KivenC
# @Date: 2020-08-02 10:39:29
# @Runtime: 396 ms
# @Memory: 13.8 MB

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, len(arr)):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    res += 1
        return res

