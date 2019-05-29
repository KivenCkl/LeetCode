
# @Title: 交换一次的先前排列 (Previous Permutation With One Swap)
# @Author: KivenC
# @Date: 2019-05-29 00:15:10
# @Runtime: 176 ms
# @Memory: 14.1 MB

class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        # 从数组的末尾开始往前遍历，保证遍历过的子数组从后往前降序排列，找到第一个不满足降序要求的数字
        # 例如对于数组 [1, 9, 4, 6, 7]，[7, 6, 4] 降序排列，因此找到的第一个数字是 9
        # 然后将该数字与它后面小于它的最大数字交换即可
        i = len(A) - 2  # 记录第一个不满足降序要求的位置
        while i >= 0 and A[i] <= A[i + 1]:
            i -= 1
        if i == -1:  # 已经是最小排列
            return A
        
        j = len(A) - 1  # 从左开始，找到第一个比 A[i] 小的最大数字，案例 [3, 1, 1, 3] -> [1, 3, 1, 3]
        while A[j] >= A[i] or A[j - 1] == A[j]:
            j -= 1
        # 进行交换
        A[i], A[j] = A[j], A[i]
        return A
