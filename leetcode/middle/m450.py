"""
m567.py
"""
from typing import List, Optional
from tool.tree import *


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return
        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            aMin = self.getMin(root.right)
            root.val = aMin.val
            root.right = self.deleteNode(root.right, aMin.val)

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMin(self, root):

        while root.left:
            root = root.left

        return root

    def run(self):
        print("run m450")

        treeDraw(self.deleteNode(treeBuild([5, 3, 6, 2, 4, None, 7]), 3))
