"""
567. 字符串的排列
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。



示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
"""
from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        end = -1
        start = end - len(s1)

        occ = dict()
        nocc = dict()
        for c in s1:
            occ[c] = occ.get(c, 0) + 1
        for i in range(len(s2)):
            end += 1
            start += 1
            nocc[s2[end]] = nocc.get(s2[end], 0) + 1
            if start >= 0:
                if nocc.get(s2[start]) - 1 > 0:
                    nocc[s2[start]] = nocc.get(s2[start]) - 1
                else:
                    nocc.pop(s2[start])
            if nocc == occ:
                return True

        return False

    def run(self):
        print("run m567")

        print(self.checkInclusion(s1="ab", s2="eidbaooo"))
