
# @Title: 最小栈 (Min Stack)
# @Author: KivenC
# @Date: 2019-07-10 14:52:28
# @Runtime: 72 ms
# @Memory: 16.1 MB

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []  # 辅助栈

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.helper and self.helper[-1] < x:
            self.helper.append(self.helper[-1])
        else:
            self.helper.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.helper.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
