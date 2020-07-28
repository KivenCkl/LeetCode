
# @Title: 按序打印 (Print in Order)
# @Author: KivenC
# @Date: 2020-07-20 18:27:02
# @Runtime: 68 ms
# @Memory: 14 MB

class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock1.acquire()
        self.lock2 = threading.Lock()
        self.lock2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
