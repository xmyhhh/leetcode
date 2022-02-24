"""
876. 链表的中间结点
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。



示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head
        i = 0

        while p1.next != None:
            p1 = p1.next
            i += 1
            if i % 2 == 0:
                p2 = p2.next
        return p2 if i % 2 == 0 else p2.next
    '''
        更好的写法：快慢指针
        def middleNode(self, head: ListNode) -> ListNode:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/lian-biao-de-zhong-jian-jie-dian-by-leetcode-solut/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''

    def run(self):
        print("run m867")
        l1 = [1, 2, 3, 4, 5, 6]

        l1_listnode = None

        for i in reversed(l1):
            if l1_listnode != None:
                l1_listnode = ListNode(i, l1_listnode)
            else:
                l1_listnode = ListNode(i)

        print(self.middleNode(head=l1_listnode))
