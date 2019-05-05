
# @Title: 加一 (Plus One)
# @Author: KivenC
# @Date: 2018-07-16 23:09:32
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if (digits[i] + 1) % 10 == 0:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
            else:
                digits[i] += 1
                return digits
