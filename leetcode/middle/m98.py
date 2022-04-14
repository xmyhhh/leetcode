"""
98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：


输入：root = [2,1,3]
输出：true
示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""
from typing import List
from tool.tree import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)

    def isValid(self, root, aMin, aMax):

        if not root:
            return True

        if aMax is not None and root.val >= aMax:
            return False
        if aMin is not None and root.val <= aMin:
            return False

        return self.isValid(root.left, aMin, root.val) and self.isValid(root.right, root.val, aMax)

    def run(self):
        print("run m98")

        print(self.isValidBST(treeBuild([0, None, -1])))
