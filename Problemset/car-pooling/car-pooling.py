
# @Title: 拼车 (Car Pooling)
# @Author: KivenC
# @Date: 2019-07-01 17:44:01
# @Runtime: 56 ms
# @Memory: 13.3 MB

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 维护一个字典，key 为站台，value 为乘客数，上客点加，下客点减
        import collections
        record = collections.defaultdict(int)
        for trip in trips:
            record[trip[2]] -= trip[0]
            record[trip[1]] += trip[0]
        tmp = 0  # 记录每站车上的乘客数
        for key in sorted(record.keys()):
            tmp += record[key]
            if tmp > capacity:
                return False
        return True
