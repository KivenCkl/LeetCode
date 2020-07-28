
# @Title: 旋转数组的最小数字 (旋转数组的最小数字  LCOF)
# @Author: KivenC
# @Date: 2020-07-22 16:26:17
# @Runtime: 44 ms
# @Memory: 13.8 MB

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # for i in range(len(numbers)-1):
        #     if numbers[i] > numbers[i+1]:
        #         return numbers[i+1]
        # return numbers[0]

        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot 
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]

