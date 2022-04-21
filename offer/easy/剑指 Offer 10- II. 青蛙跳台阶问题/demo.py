# number = list(map(int, input().split()))  # 把输入直接转成数字
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
def solver(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    if N == 2:
        return 2
    f1 = 1
    f2 = 2

    for i in range(3, N + 1):
        f3 = f1 + f2
        print(f3)
        if i == N:
            ans = f3
        f1 = f2
        f2 = f3

    return ans


def main(get_input=input):
    # N,M=map(int,get_input().split())
    N = int(get_input())

    print(solver(N))
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
