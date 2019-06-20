
# @Title: 按列翻转得到最大值等行数 (Flip Columns For Maximum Number of Equal Rows)
# @Author: KivenC
# @Date: 2019-06-14 13:54:32
# @Runtime: 196 ms
# @Memory: 14.6 MB

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 用一个元组记录每一行的特征
        # 如果第一个元素为 1 则翻转该行
        # 例如 "[1, 0, 1, 1, 1, 0, 0, 1]" 记为 (0, 1, 0, 0, 0, 1, 1, 0)
        # 具有相同特征的行代表可以通过翻转得到相同结果
        mapper = dict()
        res = 0
        for row in matrix:
            key = tuple(row) if row[0] == 0 else tuple([1 - v for v in row])
            mapper[key] = mapper.get(key, 0) + 1
            res = max(res, mapper[key])
        return res

