"""
百度春招实习第一题，完全背包_凑零钱2
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
                "3 10_组合问题_只需要计算组合的数量\n" \
                "6 20\n"

        print(self.sortArray())
