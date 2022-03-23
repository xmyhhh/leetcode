"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""


import copy
from typing import List

from tool.debug import debugTool, STACK


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = []
        track = []
        res = []
        debug = debugTool()

        def backtrack(aNums):
            debug.setnTab(stack=STACK.IN)
            if len(track) == len(aNums):
                res.append(copy.copy(track))
                debug.printWithTab("out, append, track: " + str(track))
                debug.setnTab(stack=STACK.OUT)
                return
            for i in aNums:
                if i in used:
                    continue
                used.append(i)
                track.append(i)
                debug.printWithTab("in, track: " + str(track))
                backtrack(aNums)
                track.pop()
                used.remove(i)
                debug.printWithTab("out, track: " + str(track))
            debug.setnTab(stack=STACK.OUT)
        backtrack(nums)
        return res

    def run(self):
        print("run m46")
        print(self.permute(nums=[1, 2, 3]))
