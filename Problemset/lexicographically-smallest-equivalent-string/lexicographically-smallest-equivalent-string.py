
# @Title: 按字典序排列最小的等效字符串 (Lexicographically Smallest Equivalent String)
# @Author: KivenC
# @Date: 2019-05-06 14:07:21
# @Runtime: 64 ms
# @Memory: 13.1 MB

class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        # 并查集
        tmp = {chr(i): chr(i) for i in range(ord('a'), ord('z')+1)}
        def find(x):
            if x != tmp[x]:
                tmp[x] = find(tmp[x])
            return tmp[x]
        for i in range(len(A)):
            a, b = find(A[i]), find(B[i])
            if a < b:
                tmp[b] = a
            else:
                tmp[a] = b
        print(tmp)
        return ''.join([find(s) for s in S])
