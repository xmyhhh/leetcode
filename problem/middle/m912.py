"""
m567.py
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sort(nums)

    def sort(self, nums):
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = self.sort(nums[:mid])
        right = self.sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, nums1, nums2):
        i = j = 0
        res = []
        for _ in range(len(nums1 + nums2)):

            if i == len(nums1) :
                res.append(nums2[j])
                j += 1
            elif j == len(nums2) :
                res.append((nums1[i]))
                i += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        return res

    def run(self):
        print("run m912")

        print(self.sortArray(nums=[5,1,1,2,0,0]))
