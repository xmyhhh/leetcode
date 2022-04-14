"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
"""
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        p1 = 0
        p2 = 0
        new_list = []
        for i in range(nums1_len + nums2_len):
            if p1 == nums1_len:
                new_list.append(nums2[p2])
                p2 += 1
            elif p2 == nums2_len:
                new_list.append(nums1[p1])
                p1 += 1
            else:
                if nums1[p1] < nums2[p2]:
                    new_list.append(nums1[p1])
                    p1 += 1
                elif nums1[p1] >= nums2[p2]:
                    new_list.append(nums2[p2])
                    p2 += 1

        if (nums1_len + nums2_len) % 2 == 0:
            return new_list[((nums1_len + nums2_len) // 2) - 1] * 0.5 + new_list[((nums1_len + nums2_len) // 2)] * 0.5
        else:
            return new_list[((nums1_len + nums2_len + 1) // 2) - 1]

    def run(self):
        print("run m2")

        print(self.findMedianSortedArrays(nums1=[1, 2], nums2=[3,4]))
