# number = list(map(int, input().split()))  # 把输入直接转成数字
import cProfile

MOD = 1000000007


# 定义input辅助函数（从文件加载模拟输入）
class InputHelper:
    def __init__(self, path="./input_data.txt"):
        with open(path) as file:
            self.lines = file.readlines()
        self.currentLine = -1

    def getInput(self):
        self.currentLine += 1
        return self.lines[self.currentLine]


# 定义测试样例class


# 定义处理函数
def solver(ab):
    res = 0
    ab.sort(key=lambda x: abs(x[1] - x[0]))
    maxa = ab[0][0]
    maxb = ab[0][1]
    for a, b in ab:
        if a > b:
            res = max((b + maxb) / 2, res)
        else:
            res = max((a + maxa) / 2, res)
        if a > maxa:
            maxa = a
        if b > maxb:
            maxb = b
    print(res)


def main(get_input=input):
    n = int(get_input())

    ab = []
    for i in range(n):
        ab.append(list(map(int, get_input().split())))
    solver(ab)


if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
