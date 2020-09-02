
# @Title: 机器人能否返回原点 (Robot Return to Origin)
# @Author: KivenC
# @Date: 2020-08-28 21:15:00
# @Runtime: 40 ms
# @Memory: 13.7 MB

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L')==moves.count('R') and moves.count('U')==moves.count('D')

