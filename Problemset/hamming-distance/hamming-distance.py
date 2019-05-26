
# @Title: 汉明距离 (Hamming Distance)
# @Author: KivenC
# @Date: 2019-05-25 16:32:43
# @Runtime: 48 ms
# @Memory: 13 MB

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
#         # way 1
#         c = x ^ y
#         count = 0
#         while c:
#             if c & 1:
#                 count += 1
#             c >>= 1
        
#         return count

        # way 2
        return bin(x ^ y).count('1')
