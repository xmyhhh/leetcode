"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10_组合问题_只需要计算组合的数量
输出：false
解释：从右向左读, 为 01_俄罗斯套娃信封问题(二维递增子序列) 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        if x<0:
            return False
        x_len = len(str(x))
        times = x_len//2
        a = x
        b = 0
        for i in range(times):
            b = a % 10 + b * 10
            a = (a - a % 10) / 10
        if x_len % 2 == 0 and a == b:
            return True
        elif x_len % 2 != 0 and (a - a % 10) / 10 == b:
            return True
        else:
            return False

    def run(self):
        print("run m9")
        print(self.isPalindrome(-121))
