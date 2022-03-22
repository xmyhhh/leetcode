"""
百度春招实习第一题，完全背包
"""
from typing import List


class Solution:
    def sortArray(self):
        N, W = map(int, input().split())

        dp = [0] * (W + 1)
        for _ in range(N):
            weight, value = map(int, input().split())
            for j in range(weight, W + 1):
                dp[j] = max(dp[j], dp[j - weight] + value)

        return dp[-2]

    def run(self):
        print("run m912")
        input = "3 12\n" \
                "4 20\n" \
                "3 10\n" \
                "6 20\n"

        print(self.sortArray())
