
# @Title: 任务调度器 (Task Scheduler)
# @Author: KivenC
# @Date: 2019-05-23 16:39:02
# @Runtime: 76 ms
# @Memory: 13.1 MB

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """(count [25] - 1) * (n + 1) + maxCount
        1. 假设数组 ["A","A","A","B","B","C"]，n = 2，A 的频率最高，记为 count = 3，所以两个 A 之间必须间隔 2 个任务，才能满足题意并且是最短时间（两个 A 的间隔大于 2 的总时间必然不是最短），因此执行顺序为： A->X->X->A->X->X->A，这里的 X 表示除了 A 以外其他字母，或者是待命，不用关心具体是什么，反正用来填充两个 A 的间隔的。上面执行顺序的规律是： 有 count - 1 个 A，其中每个 A 需要搭配 n 个 X，再加上最后一个 A，所以总时间为 (count - 1) * (n + 1) + 1
        2. 要注意可能会出现多个频率相同且都是最高的任务，比如 ["A","A","A","B","B","B","C","C"]，所以最后会剩下一个 A 和一个 B，因此最后要加上频率最高的不同任务的个数 maxCount
        3. 公式算出的值可能会比数组的长度小，如 ["A","A","B","B"]，n = 0，此时要取数组的长度
        """
        import collections
        counter = collections.Counter(tasks).most_common()
        max_count = counter[0][1]
        num_max = 0
        for c in counter:
            if c[1] != max_count:
                break
            num_max += 1
        return max((max_count - 1) * (n + 1) + num_max, len(tasks))
