# 已知一个背包最多能容纳体积之和为v的物品现有 n 个物品，第 i 个物品的体积为 vi , 重量为 wi求当前背包最多能装多大重量的物品?
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
def solver(v, n, goods):
    # dp[i][w] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最大价值是 dp[i][w]
    dp = [[0] * (v + 1) for _ in range(n + 1)]
    # 如果你没有把这第i个物品装入背包，那么很显然，最大价值dp[i][w]应该等于dp[i - 1][w]，继承之前的结果。
    # 如果你把这第i个物品装入了背包，那么dp[i][w]应该等于dp[i - 1][w - wt[i - 1]] + val[i - 1]。
    for i in range(1, n + 1):
        for j in range(1, v + 1):
            if j < goods[i - 1][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - goods[i - 1][0]] + goods[i - 1][1])
    return dp[n][v]


def main(get_input=input):
    goods = []
    v = int(get_input())
    n = int(get_input())
    for i in range(n):
        goods.append(list(map(int, get_input().split())))
    print(solver(v, n, goods))


if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
