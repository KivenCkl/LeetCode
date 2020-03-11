
# @Title: Dota2 参议院 (Dota2 Senate)
# @Author: KivenC
# @Date: 2019-10-22 10:55:16
# @Runtime: 72 ms
# @Memory: 13.8 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        R, D = True, True
        count = 0
        while R and D:
            R, D = False, False
            for i, s in enumerate(senate):
                if s == 'R':
                    R = True
                    if count < 0:
                        senate[i] = '0'
                    count += 1
                elif s == 'D':
                    D = True
                    if count > 0:
                        senate[i] = '0'
                    count -= 1
        return 'Radiant' if count > 0 else 'Dire'
