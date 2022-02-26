"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。



示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0, head)
        fast = slow = dummy
        i = 0

        while fast.next:
            fast = fast.next
            if i < n:
                i += 1
            else:
                slow = slow.next

        slow.next = slow.next.next

        return dummy.next

    def run(self):
        print("run m19")
        l1 = [1, 2, 3, 4, 5]

        l1_listnode = None

        for i in reversed(l1):
            if l1_listnode != None:
                l1_listnode = ListNode(i, l1_listnode)
            else:
                l1_listnode = ListNode(i)

        print(self.removeNthFromEnd(head=l1_listnode, n=2))
