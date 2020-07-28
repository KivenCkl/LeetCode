
# @Title: 不同的二叉搜索树 (Unique Binary Search Trees)
# @Author: KivenC
# @Date: 2020-07-15 13:44:40
# @Runtime: 32 ms
# @Memory: 13.7 MB

class Solution:
    def numTrees(self, n: int) -> int:
        # 假设 n 个节点存在二叉搜索树的个数为 G(n)
        # 当 1 为根节点时，其左子树节点个数为 0，右子树节点个数为 n-1
        # 当 2 为根节点时，其左子树节点个数为 1，右子树节点个数为 n-2
        # ...
        # 因此，G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-1)*G(0)
        his = [1] + [0] * n
        for i in range(1, n+1):
            his[i] = sum([his[j] * his[i-1-j] for j in range(i)])
        return his[-1]

