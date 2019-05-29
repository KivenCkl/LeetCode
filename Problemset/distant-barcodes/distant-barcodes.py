
# @Title: 距离相等的条形码 (Distant Barcodes)
# @Author: KivenC
# @Date: 2019-05-29 13:38:48
# @Runtime: 336 ms
# @Memory: 15.1 MB

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
#         # way 1
#         # 统计频数，按从多到少排列，填入列表，先填偶数位，再填奇数位
#         import collections
        
#         counter = collections.Counter(barcodes).most_common()
#         i, res = 0, [0] * len(barcodes)
#         for val, count in counter:
#             for _ in range(count):
#                 res[i] = val
#                 i += 2
#                 if i >= len(barcodes):
#                     i = 1
#         return res
    
        # way 2
        n = len(barcodes)
        if n < 3:
            return barcodes
        counter = dict()
        for barcode in barcodes:
            counter[barcode] = counter.get(barcode, 0) + 1
        v = sorted(counter.items(), key=lambda x: -x[1])
        li = []
        for val, count in v:
            li.extend([val] * count)
        res = [0] * n
        res[: : 2] = li[: (n + 1) // 2]
        res[1: : 2] = li[(n + 1) // 2:]
        return res
