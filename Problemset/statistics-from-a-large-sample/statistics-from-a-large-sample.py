
# @Title: 大样本统计 (Statistics from a Large Sample)
# @Author: KivenC
# @Date: 2019-06-25 10:17:39
# @Runtime: 56 ms
# @Memory: 12.9 MB

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mi, ma, mid, mode = -1, 0, 0, 0
        total, cnt = 0, 0
        for i, v in enumerate(count):
            if v == 0:
                continue
            # 所有数之和
            total += i * v
            # 采样数
            cnt += v
            # 众数
            if v > count[mode]:
                mode = i
            # 最小值
            if mi == -1:
                mi = i
            # 最大值
            ma = i
        if cnt % 2 == 0:
            j, k = cnt // 2, cnt // 2 + 1
        else:
            j, k = cnt // 2 + 1, cnt // 2 + 1
        for i, v in enumerate(count):
            if v == 0:
                continue
            j -= v
            k -= v
            if j <= 0:
                mid += i
                j = float('inf')
            if k <= 0:
                mid += i
                break
        return [float(mi), float(ma), total / cnt, mid / 2, float(mode)]
