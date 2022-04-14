"""
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        p = head
        i = 1
        while p.next:
            p = p.next
            i += 1
            if i == k:
                break
        if i == k:
            p = p.next
            last = self.reverseN(head, k)
            head.next = self.reverseKGroup(p, k)
            return last
        else:
            return head

    def __init__(self):
        self.succ = None

    def reverseN(self, head, n):
        if n == 1:
            self.succ = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.succ
        return last

    def run(self):
        print("run m25")
        l1 = [1, 2, 3, 4, 5]

        l1_listnode = None

        for i in reversed(l1):
            if l1_listnode != None:
                l1_listnode = ListNode(i, l1_listnode)
            else:
                l1_listnode = ListNode(i)

        print(self.reverseKGroup(l1_listnode, 2))
