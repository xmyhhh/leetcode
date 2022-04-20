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
def solver(n, m):
    from itertools import combinations
    goods = []
    for i in range(n):
        goods.append(i + 1)
    res = list(combinations(goods, m))
    for re in res:
        string = ""
        for item in re:
            string = string + " " + str(item)
        string = string[1:]

        print(string)


def main(get_input=input):
    n, m = map(int, get_input().split())

    solver(n, m)


if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
