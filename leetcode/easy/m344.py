"""
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。



示例 1：

输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)

        for idx in range(0, s_len // 2):
            a = s[idx]
            s[idx] = s[s_len - idx - 1]
            s[s_len - idx - 1] = a

    def run(self):
        print("run m344")
        print(self.reverseString(s=["H", "a", "n", "n", "a", "h"]))
