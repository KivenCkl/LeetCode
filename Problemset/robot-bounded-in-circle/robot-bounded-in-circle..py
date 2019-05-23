
# @Title: 困于环中的机器人 (Robot Bounded In Circle)
# @Author: KivenC
# @Date: 2019-05-18 16:54:26
# @Runtime: 52 ms
# @Memory: 12.9 MB

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 仅当循环一次后方向仍向北且有位移才不会困于环中，不然循环四次之后都会达到同一个状态(同方向，同坐标）
        x, y = 0, 0  # 位置
        dx, dy = 0, 1  # 方向
        for c in instructions:
            if c == 'L':
                dx, dy = -dy, dx
            elif c == 'R':
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
