
# @Title: 1比特与2比特字符 (1-bit and 2-bit Characters)
# @Author: KivenC
# @Date: 2018-07-12 21:25:38
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        k = 0
        while k < len(bits)-1:
            if bits[k] == 1:
                k += 2
            else:
                k += 1
        if k == len(bits)-1 and bits[k] == 0:
            return True
        else:
            return False
