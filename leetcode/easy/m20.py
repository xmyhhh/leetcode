"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
"""
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        left = ['[', '{', '(']
        right = [']', '}', ')']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) == 0 or left.index(stack.pop()) != right.index(c):
                    return False
        # if len(stack) == 0:   # 这个地方可以简写为   return not stack  因为空列表返回False
        #     return True
        return not stack
    def run(self):
        print("run m20")
        print(self.isValid("{[]}"))
