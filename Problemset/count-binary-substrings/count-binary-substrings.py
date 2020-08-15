
# @Title: 计数二进制子串 (Count Binary Substrings)
# @Author: KivenC
# @Date: 2020-08-10 15:17:47
# @Runtime: 168 ms
# @Memory: 14.1 MB

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # cur_char, cur_count = s[0], 1
        # pre_char, pre_count = '', 0
        # res = 0
        # for i in range(1, len(s)):
        #     if s[i] == cur_char:
        #         cur_count += 1
        #     else:
        #         if pre_count > 0:
        #             res += min(pre_count, cur_count)
        #         pre_char, pre_count = cur_char, cur_count
        #         cur_char, cur_count = s[i], 1
        # res += min(pre_count, cur_count)
        # return res

        last, cur, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                last, cur = cur, 1
            if cur <= last:
                res += 1
        return res

