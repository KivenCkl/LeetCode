
# @Title: 跳水板 (Diving Board LCCI)
# @Author: KivenC
# @Date: 2020-07-08 14:45:30
# @Runtime: 84 ms
# @Memory: 17.7 MB

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        elif shorter == longer:
            return [shorter * k]
        else:
            return [longer * i + shorter * (k - i) for i in range(k+1)]
