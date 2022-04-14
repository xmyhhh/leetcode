"""
189. 轮转数组
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。



示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        num_boxs = nums[len(nums) - k:]
        nums[k:] = nums[0:len(nums) - k]
        nums[0:k] = num_boxs
        '''
        更好的做做法
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:n] + nums[0:n-k]
        '''

    def run(self):
        print("run m189")
        print(self.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
