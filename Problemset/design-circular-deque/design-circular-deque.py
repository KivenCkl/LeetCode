
# @Title: 设计循环双端队列 (Design Circular Deque)
# @Author: KivenC
# @Date: 2019-10-22 11:25:07
# @Runtime: 88 ms
# @Memory: 14.1 MB

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = []
        self.size = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == self.size:
            return False
        self.deque.insert(0, value)
        return True
            
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == self.size:
            return False
        self.deque.append(value)
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.deque:
            return False
        self.deque.pop(0)
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.deque:
            return False
        self.deque.pop()
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.deque:
            return -1
        return self.deque[0]
        
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.deque:
            return -1
        return self.deque[-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self.deque
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque) == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
