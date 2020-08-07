
# @Title: 找出数组游戏的赢家 (Find the Winner of an Array Game)
# @Author: KivenC
# @Date: 2020-08-02 10:55:37
# @Runtime: 1664 ms
# @Memory: 24.5 MB

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr) - 1:
            return max(arr)
        tmp = k
        while tmp > 0:
            if arr[0] > arr[1]:
                v = arr.pop(1)
                arr.append(v)
                tmp -= 1
            else:
                v = arr.pop(0)
                arr.append(v)
                tmp = k - 1
        return arr[0]
            
