
# @Title: 你能从盒子里获得的最大糖果数 (Maximum Candies You Can Get from Boxes)
# @Author: KivenC
# @Date: 2020-07-15 18:12:55
# @Runtime: 968 ms
# @Memory: 26 MB

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res = 0
        key = []
        may_open_box = []
        queue = initialBoxes
        while queue:
            box = queue.pop()
            if status[box] or box in key:
                res += candies[box]
                key += keys[box]
                queue += containedBoxes[box]
            else:
                if box not in may_open_box:
                    queue.insert(0, box)
                    may_open_box.append(box)
        return res
                
