
# @Title: 外观数列 (Count and Say)
# @Author: KivenC
# @Date: 2019-02-25 11:05:18
# @Runtime: 52 ms
# @Memory: 6.4 MB

class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        ans = '1'
        for _ in range(n-1):
            cur = ''
            count = 1
            for ind, num in enumerate(ans):
                if ind == len(ans) - 1 or num != ans[ind + 1]:
                    cur += str(count) + num
                    count = 1
                else:
                    count += 1
            ans = cur
        return ans
