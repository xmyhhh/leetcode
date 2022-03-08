"""
322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return 1
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            dp[coin] = 1
        for i in range(1, (amount + 1)):
            dp[i] = min(dp[i - coin] for coin in coins)
            aaaa
        return dp[amount]
    def run(self):
        print("run m322")

        print(self.coinChange(coins=[2], amount=3))
