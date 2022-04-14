# /*
# 题目描述：
# 小明在尝试把一些分子为1的分数（1/x）转化为小数。使用普通计算器的除法功能可以实现，但是保留的小数位数非常有限。而小明希望得到n位小数，而且要从小数点后面第d位开始的n位小数。
# 例如，x=13, d=4, n=3时，1/13=0.07692307692……，从小数点后第四位开始取三位数，答案是923。现在小明想要计算一些数更大的情况（2 <= x <= 10000, 1 <= d <= 1000000000, 1 <= n <= 10000），请你写个程序帮帮他。
#  */
#
#
# #include <algorithm>
# #include <iostream>
# #include <string>
#
# int main() {
# //    int x = 13, d = 4, n = 3;
#     int x, d, n;
#     std::cin >> x >> d >> n;
#     double r = 1.0 / x;
#     std::string str = std::to_string(r);
#     auto dot = str.find(".");
#     std::cout << str.substr(dot + d, n) << std::endl;
#     return 0;
# }
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


# 定义处理函数
def solver(x, d, n):
    start = 0
    current_num = 1
    while (start < d):
        if (current_num < x):
            current_num = current_num * 10
            start += 1
        elif (current_num > x):
            current_num = current_num % x
            current_num = current_num * 10
            start += 1

    res = []

    while (start < (d + n)):
        if (current_num < x):
            current_num = current_num * 10
            res.append(0)
            start += 1

        elif (current_num > x):
            res.append(current_num // x)
            current_num = current_num % x
            current_num = current_num * 10
            start += 1

    return res


def main(get_input=input):
    x, d, n = map(int, get_input().split())

    print(solver(x, d, n))
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
