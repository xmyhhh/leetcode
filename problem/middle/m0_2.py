"""
百度春招实习第二题，双指针
"""
from typing import List


class Solution:
    def sortArray(self):
        # nums = input()
        nums = "246135"
        numsList = [0] * len(nums)
        for i in range(len(nums)):
            numsList[i] = nums[i]
        K = numsList[0]
        resLen = len(nums) - int(K)
        res = ""
        last = 0

        for i in range(resLen):
            print(numsList[last:len(nums) - resLen + 1 + i])
            res += max(numsList[last:len(nums) - resLen + 1 + i])
            last = numsList.index(max(numsList[last:len(nums) - resLen + 1 + i])) + 1
        return res

    def run(self):
        print("run m0_2")

        print(self.sortArray())
