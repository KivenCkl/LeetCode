
# @Title: 千位分隔数 (Thousand Separator)
# @Author: KivenC
# @Date: 2020-08-23 01:03:42
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def thousandSeparator(self, n: int) -> str:
        # return format(n, ',').replace(',', '.')
        s = str(n)
        count = len(s)
        res = ''
        for c in s:
            res += c
            count -= 1
            if count > 0 and count % 3 == 0:
                res += '.'
        return res

