"""
234. 回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p1 = slow = fast = head
        while (fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        p2 = self.reverse(slow.next)
        while p2:
            if p1.val != p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True

    def reverse(self, head):
        current = head
        pre = None
        while (current):
            nxt = current.next
            current.next = pre
            pre = current
            current = nxt
        return pre

    def run(self):
        print("run m234")
        l1 = [1, 2, 2, 1]

        l1_listnode = None

        for i in reversed(l1):
            if l1_listnode != None:
                l1_listnode = ListNode(i, l1_listnode)
            else:
                l1_listnode = ListNode(i)

        print(self.isPalindrome(l1_listnode))
