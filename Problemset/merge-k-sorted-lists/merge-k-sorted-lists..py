
# @Title: 合并K个排序链表 (Merge k Sorted Lists)
# @Author: KivenC
# @Date: 2019-01-27 14:26:35
# @Runtime: 156 ms
# @Memory: 10.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        elif len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            left_half = self.mergeKLists(lists[:mid])
            right_half = self.mergeKLists(lists[mid:])
            ans = self.merge_sorted_list(left_half, right_half)

            return ans

    def merge_sorted_list(self, l1, l2):
        newNode = ListNode(0)
        retNode = newNode
        while l1 and l2:
            if l1.val >= l2.val:
                newNode.next = l2
                l2 = l2.next
            else:
                newNode.next = l1
                l1 = l1.next
            newNode = newNode.next
        if not l1:
            newNode.next = l2
        if not l2:
            newNode.next = l1

        return retNode.next
