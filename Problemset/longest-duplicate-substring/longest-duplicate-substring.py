
# @Title: 最长重复子串 (Longest Duplicate Substring)
# @Author: KivenC
# @Date: 2019-05-29 14:47:19
# @Runtime: 1800 ms
# @Memory: 24.8 MB

class Solution:
#     way 1
#     超时
#     def __init__(self):
#         import collections
#         self.BASE = 26
#         self.MOD = (1 << 61) - 1
        
#     def longestDupSubstring(self, S: str) -> str:
#         # 二分查找最长可能长度的重复子串
#         lo, hi, res = 2, len(S) - 1, ""
#         while lo <= hi:
#             mid = lo + (hi - lo) // 2
#             sub = self.rabinKarp(S, mid)
#             if sub != "":
#                 lo, res = mid + 1, sub
#             else:
#                 hi = mid - 1
#         return res
    
#     def rabinKarp(self, S: str, k: int) -> str:
#         # 应用 Rabin-Karp 算法判断子串是否匹配
#         # Hash(s[0:k]) = s[0] ∗ b**(k−1) + s[1] ∗ b**(k−2) + ... + s[k−1] ∗ b**0
#         # Hash(s[1:k+1]) = (Hash(s[0:k]) - s[0] * b**(k-1)) * b + s[k] * b**0
#         h = pow(self.BASE, k - 1, self.MOD)  # 记录 b**(k-1)
#         mapper = collections.defaultdict(list)  # key 为子串的 hash 值，value 为 hash 碰撞的子串结束序号列表
#         hash_val = 0
#         for i in range(len(S)):
#             if i >= k:
#                 pre_code = ord(S[i - k]) - ord('a')
#                 hash_val = (hash_val + self.MOD - (pre_code * h) % self.MOD) % self.MOD  # 防止为负数
            
#             code = ord(S[i]) - ord('a')
#             hash_val = (hash_val * self.BASE + code) % self.MOD

#             if i >= k - 1:
#                 if hash_val in mapper:  # 考虑 hash 碰撞的情况
#                     subStr = S[i - k + 1:i + 1]
#                     for ind in mapper[hash_val]:  # 验证两子串是否相等
#                         if S[ind - k + 1:ind + 1] == subStr:
#                             return subStr
#                 mapper[hash_val].append(i)
#         return ""
 
#         way 2
    def longestDupSubstring(self, S: str) -> str:
        import functools
        A = [ord(c) - ord('a') for c in S]
        base = 26
        mod = 2**63 - 1
        n = len(S)
        
        def rabinKarp(k):
            p = pow(base, k, mod)
            cur = functools.reduce(lambda x, y: (x * base + y) % mod, A[: k])
            seed = {cur}
            for index in range(k, n):
                cur = (cur * base + A[index] - A[index-k] * p) % mod
                if cur in seed:
                    return index - k + 1
                seed.add(cur)
            return -1
        
        low, high = 0, n
        res = 0
        while low < high:
            mid = (low + high + 1) // 2
            pos = rabinKarp(mid)
            if pos != -1:
                low = mid
                res = pos
            else:
                high = mid - 1
        return S[res: res+low]
