"""
m567.py
"""
from typing import List


class Solution:
    def sortArray(self):
        # nums = input()
        nums = "338638"
        numsList = [0] * len(nums)
        for i in range(len(nums)):
            numsList[i] = nums[i]
        K = numsList[0]
        resLen = len(nums) - int(K)
        res = ""

        last = 0
        for i in range(resLen):
            res += max(numsList[last:resLen + i+1])
            last = numsList.index(max(numsList[last:resLen + i+1])) + 1
        return res

    def run(self):
        print("run m0_2")

        print(self.sortArray())
