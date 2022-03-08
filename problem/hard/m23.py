"""
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

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
        print(self.mergeKLists(l1_listnode, l2_listnode))
