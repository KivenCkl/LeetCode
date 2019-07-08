
# @Title: 分糖果 II (Distribute Candies to People)
# @Author: KivenC
# @Date: 2019-07-03 18:34:09
# @Runtime: 44 ms
# @Memory: 13 MB

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
#         # way 1
#         # 假设总分发次数为 k，则总共需要的糖果数为 S(k) = (1 + k) * k / 2
#         # 由于最后一次可以不发满，无论剩多少都会给最后一个小朋友，所以 S(k-1) < candies <= S(k)
#         # 通过该不等式可以算出 (-1+(1+8*candies)^(1/2))/2 <= k < (1+(1+8*candies)^(1/2))/2
#         import math
#         k = math.ceil((math.sqrt(1 + 8 * candies) - 1) / 2)
#         i = 0
#         res = [0] * num_people
        
#         # 因为不知道最后一次需要发多少糖果，因此循环分发 k - 1 次
#         while k > 1:
#             res[i % num_people] += i + 1
#             i += 1
#             candies -= i
#             k -= 1
#         # 将剩余糖果发掉
#         res[i % num_people] += candies
#         return res
    
#         # way 2
#         # 直接模拟整个过程
#         k = 0
#         i = 0
#         arr = [0] * num_people
        
#         while(True):
#             k += 1

#             if(k <= candies):
#                 arr[i] += k
#                 candies -= k
#             else:
#                 arr[i] += candies
#                 break
            
#             i = (i + 1) % num_people
            
#         return arr

        # way 3
        # 优化 way 1
        import math
        k = math.ceil((math.sqrt(1 + 8 * candies) - 1) / 2)
        i, j = k // num_people, k % num_people  # 前 j 个小朋友发了 i+1 次，剩下的发了 i 次
        if j == 0:
            j = num_people
            i -= 1
        remain = candies - k * (k - 1) // 2  # 最后一次发的糖果数
        res = []
        
        for ind in range(1, num_people+1):
            if ind < j:
                res.append((i + 1) * i // 2 * num_people + (i + 1) * ind)
            else:
                tmp = (i * (i - 1) // 2 * num_people if i > 0 else 0) + i * ind
                if ind == j:
                    res.append(tmp + remain)
                else:
                    res.append(tmp)
        return res
