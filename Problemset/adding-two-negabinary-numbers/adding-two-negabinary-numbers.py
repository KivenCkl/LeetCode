
# @Title: 负二进制数相加 (Adding Two Negabinary Numbers)
# @Author: KivenC
# @Date: 2019-06-14 14:54:33
# @Runtime: 52 ms
# @Memory: 12.9 MB

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 对 arr1 和 arr2 从后往前依次相加，逢二进一，构造新列表
        i, carry = -1, 0  # i 表示下标，carry 表示进位
        l1, l2 = len(arr1), len(arr2)
        res = []
        while i + l1 > -1 or i + l2 > -1 or carry != 0:
            tmp = -carry
            if i + l1 > -1:
                tmp += arr1[i]
            if i + l2 > -1:
                tmp += arr2[i]
            res.append(tmp % 2)
            carry = tmp // 2
            i -= 1
        while res[-1] == 0 and len(res) > 1:
            res.pop()
        return res[::-1]
