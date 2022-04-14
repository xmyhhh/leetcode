"""
160. 相交链表
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

图示两个链表在节点 c1 开始相交：



题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

自定义评测：

评测系统 的输入如下（你设计的程序 不适用 此输入）：

intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
listA - 第一个链表
listB - 第二个链表
skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #不太好写测试
        pass
    def run(self):
        print("run m160")
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        l3 = [5, 6, 4]
        l1_listnode = None
        l2_listnode = None
        l3_listnode = None
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
        for i in reversed(l3):
            if l3_listnode != None:
                l3_listnode = ListNode(i, l3_listnode)
            else:
                l3_listnode = ListNode(i)
        print(self.getIntersectionNode(l1_listnode, l2_listnode))
