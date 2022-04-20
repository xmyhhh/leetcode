# number = list(map(int, input().split()))  # 把输入直接转成数字
import cProfile

MOD = 998244353


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
def solver(N, a, b, c, d):
    def combinations(m, n):  # 排列，计算C（m n）,n是总数，m是待选数
        assert m <= n
        import math
        return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

    return combinations(a, N * N) * combinations(b, N * N - a) * combinations(c, N * N - a - b) % MOD


def main(get_input=input):
    N, a, b, c, d = map(int, get_input().split())

    print(solver(N, a, b, c, d))
    pass


if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
