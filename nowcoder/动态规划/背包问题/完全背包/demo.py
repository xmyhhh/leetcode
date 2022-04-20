# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。假设每一种面额的硬币有无限个。
import cProfile

MOD = 1e+3

# 定义input辅助函数（从文件加载模拟输入）
class InputHelper:
    def __init__(self, path="./input_data.txt"):
        with open(path) as file:
            self.lines = file.readlines()
        self.currentLine = -1

    def getInput(self):
        self.currentLine += 1
        return self.lines[self.currentLine]

# 定义处理函数
def solver(amount, coins):
    coins_num = len(coins)
    # 定义DP：若只使用 coins 中的前 i 个硬币的面值，若想凑出金额 j，有 dp[i][j] 种凑法
    dp = [[0] * (amount + 1) for _ in range(coins_num + 1)]
    # base case：为dp[0][..] = 0， dp[..][0] = 1。因为如果不使用任何硬币面值，就无法凑出任何金额；如果凑出的目标金额为0，那么“无为而治”就是唯一的一种凑法
    for i in range(amount + 1):
        dp[0][i] = 0
    for i in range(coins_num + 1):
        dp[i][0] = 1
    # 状态转移：
    # 如果你不把这第 i 个物品装入背包，也就是说你不使用 coins[i-1] 这个面值的硬币，那么凑出面额 j 的方法数 dp[i][j] 应该等于 dp[i-1][j]，继承之前的结果。
    # 如果你把这第 i 个物品装入了背包，也就是说你使用 coins[i-1] 这个面值的硬币，那么 dp[i][j] 应该等于 dp[i][j-coins[i-1]]。
    for i in range(1, coins_num + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                # 我们想求的 dp[i][j] 是「共有多少种凑法」，所以 dp[i][j] 的值应该是以上两种选择的结果之和
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[coins_num][amount]

def main(get_input=input):
    amount = int(get_input())

    coins = (list(map(int, get_input().split())))
    print(solver(amount, coins))

if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
