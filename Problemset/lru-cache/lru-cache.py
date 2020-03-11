
# @Title: LRU缓存机制 (LRU Cache)
# @Author: KivenC
# @Date: 2019-07-10 19:25:02
# @Runtime: 124 ms
# @Memory: 21.5 MB

# way 1
# from typing import Optional
# class ListNode:
#     """定义双链表"""
#     def __init__(self, key: Optional[int] = None, value: Optional[int] = None):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}  # key 为 key，value 为 node
#         self.head = ListNode()
#         self.tail = ListNode()
        
#         # 连接头尾哨兵结点
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key: int) -> int:
#         # key 不在缓存中，则返回 -1
#         if key not in self.cache:
#             return -1
#         # 否则将其挪至链表的尾部，返回 value
#         self.move_node_to_tail(key)
#         return self.cache[key].value

#     def put(self, key: int, value: int) -> None:
#         # key 不在缓存中
#         if key not in self.cache:
#             # 当缓存容量达到上限，删除最近最少使用的结点（头结点）
#             if len(self.cache) == self.cap:
#                 del self.cache[self.head.next.key]
#                 self.head.next = self.head.next.next
#                 self.head.next.prev = self.head
#             new_node = ListNode(key, value)  # 添加新结点
#             self.cache[key] = new_node  # 记录于缓存中
            
#             # 将该新结点插入至尾部
#             new_node.prev = self.tail.prev
#             new_node.next = self.tail
#             self.tail.prev.next = new_node
#             self.tail.prev = new_node
#         # key 存在于缓存中，则更新其值，并将其挪至链表的尾部
#         else:
#             self.cache[key].value = value
#             self.move_node_to_tail(key)
    
#     def move_node_to_tail(self, key: int) -> None:
#         node = self.cache[key]  # 找到 key 对应的结点
        
#         # 将该结点从原来的位置取出
#         node.next.prev = node.prev
#         node.prev.next = node.next
        
#         # 插入至尾节点
#         node.prev = self.tail.prev
#         node.next = self.tail
#         self.tail.prev.next = node
#         self.tail.prev = node


# way 2
import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            del self.dic[key]
        elif len(self.dic) == self.cap:
            self.dic.popitem(False)
        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
