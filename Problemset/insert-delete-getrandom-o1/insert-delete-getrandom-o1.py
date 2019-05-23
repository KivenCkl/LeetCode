
# @Title: 常数时间插入、删除和获取随机元素 (Insert Delete GetRandom O(1))
# @Author: KivenC
# @Date: 2019-03-26 20:43:03
# @Runtime: 384 ms
# @Memory: 16.8 MB

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.values:
            return False
        else:
            self.values.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.values:
            self.values.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        from random import choice
        return choice(list(self.values))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
