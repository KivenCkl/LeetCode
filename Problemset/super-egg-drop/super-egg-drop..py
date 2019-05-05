
# @Title: 鸡蛋掉落 (Super Egg Drop)
# @Author: KivenC
# @Date: 2019-03-02 19:23:14
# @Runtime: 56 ms
# @Memory: 13.3 MB

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        '''
        基于动态规划：假设 f {n,m} 表示 n 层楼、m 个鸡蛋时找到最高楼层的最少尝试次数。当第一个鸡蛋从第 i 层扔下，如果碎了，还剩 m-1 个鸡蛋，为确定下面楼层中的安全楼层，还需要 f {i-1,m-1} 次，找到子问题；不碎的话，上面还有 n-i 层，还需要 f [n-i,m] 次，又一个子问题。 状态转移方程如下： f {n, m} = min (1 + max (f {n - 1, m - 1}, f {n - i, m}) ) 其中： i 为 (1, n), f {i, 1} = 1
        基于数学方程的方法(对于K=2的情形)：假设最少尝试次数为 x，那么，第一个鸡蛋必须要从第 x 层扔下，因为：如果碎了，前面还有 x - 1 层楼可以尝试，如果没碎，后面还有 x-1 次机会。如果没碎，第一个鸡蛋，第二次就可以从 x +（x - 1）层进行尝试，为什么是加上 x - 1，因为，当此时，第一个鸡蛋碎了，第二个鸡蛋还有可以从 x+1 到 x + (x - 1) - 1 层进行尝试，有 x - 2 次。如果还没碎，那第一个鸡蛋，第三次从 x + (x - 1) + (x - 2) 层尝试。碎或者没碎，都有 x - 3 次尝试机会，依次类推。那么，x 次的最少尝试，可以确定的最高的楼层是多少呢？ x + (x - 1) + (x - 2) + … + 1 = x (x+1) / 2 那反过来问，当最高楼层是 100 层，最少需要多少次呢？x (x+1)/2 >= 100, 得到 x>=14，最少要尝试 14 次。
        '''
        '''
        res = [[0 for _ in range(N+1)] for _ in range(K+1)]
        for n in range(N+1):
            res[1][n] = n
        for k in range(2, K+1):
            for n in range(1, N+1):
                min_res = float('inf')
                for i in range(1, n+1):
                    min_res = min(min_res, 1 + max(res[k-1][i-1], res[k][n-i]))
                res[k][n] = min_res
        return res[K][N]
        '''
        moves = 0
        dp = [0 for _ in range(K+1)]
        while dp[K] < N:
            # 逆序从K---1,dp[i] = dp[i]+dp[i-1] + 1 相当于上次移动后的结果,dp[]函数要理解成抽象出来的一个黑箱子函数,跟上一次移动时鸡蛋的结果有关系
            for i in range(K, 0, -1):
                dp[i] += dp[i-1] + 1
                # 以上计算式，是从以下转移方程简化而来
                # dp[moves][k] = 1 + dp[moves-1][k-1] + dp[moves-1][k]
                # 假设 dp[moves-1][k-1] = n0, dp[moves-1][k] = n1
                # 首先检测，从第 n0+1 楼丢下鸡蛋会不会破。
                # 如果鸡蛋破了，F 一定是在 [1：n0] 楼中，
                # 		利用剩下的 moves-1 次机会和 k-1 个鸡蛋，可以把 F 找出来。
                # 如果鸡蛋没破，假如 F 在 [n0+2:n0+n1+1] 楼中
                # 		利用剩下的 moves-1 次机会和 k 个鸡蛋把，也可以把 F 找出来。
                # 所以，当有 moves 个放置机会和 k 个鸡蛋的时候
                #/ F 在 [1, n0+n1+1] 中的任何一楼，都能够被检测出来。
            moves += 1
        return moves
