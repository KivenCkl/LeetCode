
# @Title: 绝对值表达式的最大值 (Maximum of Absolute Value Expression)
# @Author: KivenC
# @Date: 2019-08-17 16:43:59
# @Runtime: 408 ms
# @Memory: 24.2 MB

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # 参考：https://leetcode-cn.com/problems/maximum-of-absolute-value-expression/solution/python-jie-fa-bao-li-shu-xue-by-jiayangwu/
        
        # op = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        # max_li = [-float('inf')] * 4
        # min_li = [float('inf')] * 4
        # for i, (x, y) in enumerate(zip(arr1, arr2)):
        #     for j, (op1, op2) in enumerate(op):
        #         tmp = x + op1 * y + op2 * i
        #         max_li[j] = max(tmp, max_li[j])
        #         min_li[j] = min(tmp, min_li[j])
        # return max([x - y for x, y in zip(max_li, min_li)])
    
        A, B, C, D= [], [], [], []
        for i in range(len(arr1)):
            x, y = arr1[i], arr2[i]
            A.append(x + y + i)
            B.append(x + y - i)
            C.append(x - y + i)
            D.append(x - y - i)
            
        a = max(A) - min(A)
        b = max(B) - min(B)
        c = max(C) - min(C)
        d = max(D) - min(D)        
        return max(a, b, c, d)
            
