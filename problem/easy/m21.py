"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy

        while list1 or list2:
            if not list1 and list2:
                p.next = list2
                p = p.next
                list2 = list2.next
            elif list1 and not list2:
                p.next = list1
                p = p.next
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    p.next = list1
                    p = p.next
                    list1 = list1.next
                else:
                    p.next = list2
                    p = p.next
                    list2 = list2.next
        return dummy.next
    def run(self):
        print("run m21")
        l1 = [1, 2, 4]
        l2 = [1, 3, 4]
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
        print(self.mergeTwoLists(l1_listnode, l2_listnode))
