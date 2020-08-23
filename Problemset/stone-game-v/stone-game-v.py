
# @Title: 石子游戏 V (Stone Game V)
# @Author: KivenC
# @Date: 2020-08-23 14:14:28
# @Runtime: 4936 ms
# @Memory: 38.8 MB

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        self.sums = [0]
        for t in stoneValue:
            self.sums.append(self.sums[-1]+t)
        
        @functools.lru_cache(None)
        def deal(start, end):
            if end == start:
                return 0
            
            to_ret = 0
            for mid in range(start+1, end+1):
                # l : start : mid-1
                # r : mid   : end
                suml = self.sums[mid] - self.sums[start]
                sumr = self.sums[end+1] - self.sums[mid]
                if suml <= sumr:
                    to_ret = max(to_ret, suml+deal(start, mid-1))
                if sumr <= suml:
                    to_ret = max(to_ret, sumr+deal(mid, end))
            return to_ret
        
        return deal(0, len(stoneValue)-1)
        
