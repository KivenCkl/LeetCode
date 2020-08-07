
# @Title: 猜数字游戏 (Bulls and Cows)
# @Author: KivenC
# @Date: 2020-08-06 16:02:55
# @Runtime: 48 ms
# @Memory: 13.7 MB

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # record = collections.defaultdict(int)
        # bull, cow = 0, 0
        # for num in secret:
        #     record[num] += 1
        # for c1, c2 in zip(secret, guess):
        #     if c1 == c2:
        #         bull += 1
        #         if record[c1] > 0:
        #             record[c1] -= 1
        #         else:
        #             cow -= 1
        #     else:
        #         if c2 in record and record[c2] > 0:
        #             record[c2] -= 1
        #             cow += 1
        # return f"{bull}A{cow}B"

        bull = 0
        record = {}
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                bull += 1
            else:
                record[c1] = record.get(c1, 0) + 1
                record[c2] = record.get(c2, 0) - 1
        cow = len(secret) - bull - sum(filter(lambda x: x > 0, record.values()))
        return f"{bull}A{cow}B"
        
