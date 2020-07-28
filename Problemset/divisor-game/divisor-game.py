
# @Title: 除数博弈 (Divisor Game)
# @Author: KivenC
# @Date: 2020-07-24 16:38:07
# @Runtime: 40 ms
# @Memory: 13.6 MB

class Solution:
    def divisorGame(self, N: int) -> bool:
        # 因为先手为偶数的话，先手只需要让自己每步都保持偶数
        # 那么他可以通过让对手得到的数为奇数，比如偶数-1就是奇数
        # 对手拿到奇数，那么能整除的只有奇数，奇数-奇数又回到了偶数
        # 最后先手一定会得到最小的偶数2，然后-1让对手得到1，对手无解，必胜
        return not N & 1

