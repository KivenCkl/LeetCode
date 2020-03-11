
# @Title: 根据身高重建队列 (Queue Reconstruction by Height)
# @Author: KivenC
# @Date: 2019-07-15 11:15:03
# @Runtime: 156 ms
# @Memory: 13.5 MB

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 假设候选队列为 A，已经站好队的队列为 B.
        # 从 A 里挑身高最高的人 x 出来，插入到 B.
        # 因为 B 中每个人的身高都比 x 要高，因此 x 插入的位置，就是看 x 前面应该有多少人就行了。
        # 比如 x 前面有 5 个人，那 x 就插入到队列 B 的第 5 个位置。
        res = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for h, k in people:
            res.insert(k, [h, k])
        return res
