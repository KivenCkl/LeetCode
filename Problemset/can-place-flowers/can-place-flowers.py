
# @Title: 种花问题 (Can Place Flowers)
# @Author: KivenC
# @Date: 2018-07-16 13:48:02
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        new_f = [0] + flowerbed + [0, 1]
        count = 0
        for flower in new_f:
            if flower == 1:
                n -= (count-1)//2
                count = 0
            else:
                count += 1
        if n > 0:
            return False
        else:
            return True
