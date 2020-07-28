
# @Title: 两数之和 II - 输入有序数组 (Two Sum II - Input array is sorted)
# @Author: KivenC
# @Date: 2020-07-20 18:11:45
# @Runtime: 44 ms
# @Memory: 14.2 MB

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dic = {}
        # for i, v in enumerate(numbers, start=1):
        #     if target-v in dic:
        #         return [dic[target-v], i]
        #     else:
        #         dic[v] = i

        i, j = 0, len(numbers)-1
        while j > i:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []

