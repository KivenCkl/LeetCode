
# @Title: K 次操作转变字符串 (Can Convert String in K Moves)
# @Author: KivenC
# @Date: 2020-08-08 23:09:46
# @Runtime: 348 ms
# @Memory: 14.2 MB

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        res = {}
        for a, b in zip(s, t):
            dis = ord(b) - ord(a)
            if dis < 0:
                dis += 26
            if dis > 0:
                res[dis] = res.get(dis, 0) + 1
        for i, v in res.items():
            if 26 * (v - 1) + i > k:
                return False
        return True
            
