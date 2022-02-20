"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = ListNode()
        head = value #初始化头节点
        add_flag = False  # 进位标志
        while l1 != None or l2!= None:
            value.next = ListNode(((l1.val if l1 else 0) + (l2.val if l2 else 0) + (
                1 if add_flag else 0)) % 10)
            value = value.next
            if ((l1.val if l1 else 0) + (l2.val if l2 else 0) + (1 if add_flag else 0)) > 9:
                add_flag = True
            else:
                add_flag = False
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if add_flag:
            value.next = ListNode(1)
        return head.next




    def run(self):
        print("run m2")
        l1 = [2,4,3]
        l2 = [5,6,4]
        l1_listnode = None
        l2_listnode = None
        for i in reversed(l1):
            if l1_listnode != None:
                l1_listnode = ListNode(i, l1_listnode)
            else:
                l1_listnode = ListNode(i)
        for i in reversed(l2):
            if l2_listnode != None:
                l2_listnode = ListNode(i, l2_listnode)
            else:
                l2_listnode = ListNode(i)
        print(self.addTwoNumbers(l1_listnode, l2_listnode))
