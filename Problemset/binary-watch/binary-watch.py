
# @Title: 二进制手表 (Binary Watch)
# @Author: KivenC
# @Date: 2020-08-18 23:43:27
# @Runtime: 44 ms
# @Memory: 13.7 MB

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # res = []
        # hour_visited = set()
        # minute_visited = set()

        # def traverse(num: int, hour: int, minute: int, which: int) -> None:
        #     # 将 10 盏灯看作一个列表，which 用于记录当前遍历位置，防止重复
        #     if hour > 11 or minute > 59:
        #         return
        #     if num == 0:
        #         res.append(f"{hour}:{minute:02}")
        #         return
        #     for h in range(which, 4):
        #         if h not in hour_visited:
        #             hour_visited.add(h)
        #             traverse(num-1, hour+int(pow(2, h)), minute, h+1)
        #             hour_visited.remove(h)
            
        #     for m in range(max(which, 4), 10):
        #         if m not in minute_visited:
        #             minute_visited.add(m)
        #             traverse(num-1, hour, minute+int(pow(2, m-4)), m+1)
        #             minute_visited.remove(m)
            
        # traverse(num, 0, 0, 0)
        # return res

        if num < 0:
            return []
        # 一共只有10个灯
        res, hour, minute = [], [1, 2, 4, 8], [1, 2, 4, 8, 16, 32]
        def traceback(num: int, index: int, status: List[int]) -> None:
            """
            num : 还剩下的可点亮的灯的数量
            index: 是当前选择点亮哪一个灯
            status: 记录是哪些位置的灯被点亮了
            """
            if num == 0:  # 没有可以点亮的灯了，记录当前结果，并返回
                h = sum([i * j for i, j in zip(hour, status[:4])])
                m = sum([i * j for i, j in zip(minute, status[4:])])
                if h < 12 and m < 60:
                    res.append(f"{h}:{m:02}")
                return
            for i in range(index, 10):
                status[i] = 1  # 做出下一步的选择
                traceback(num-1, i+1, status)  # 在剩下的灯里面去点亮num-1个灯
                status[i] = 0  # 返回到上一步选择时的状态            
        
        traceback(num, 0, [0] * 10)
        return res

