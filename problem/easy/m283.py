"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        n = len(nums)
        for num in nums:
            if num != 0:
                nums[k] = num
                k+=1
        nums[k:n] = [0] * (n - k)
        '''
        n = len(nums)
        k = 0
        for i,v in enumerate(nums):
            if v!=0:
                nums[k]=v
                k+=1
        nums[k:n]=[0]*(n-k)
        '''
    def run(self):
        print("run m283")
        print(self.moveZeroes([0, 1, 0, 3, 12]))
