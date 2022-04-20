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


# 定义处理函数
def solver(A, B, a, b):
    def get_greatest_common_divisor(a, b):  ##最大公约数
        if a == b:
            return a
        if (a & 1) == 0 and (b & 1) == 0:
            return get_greatest_common_divisor(a >> 1, b >> 1) << 1
        elif (a & 1) == 0 and (b & 1) != 0:
            return get_greatest_common_divisor(a >> 1, b)
        elif (a & 1) != 0 and (b & 1) == 0:
            return get_greatest_common_divisor(a, b >> 1)
        else:
            big = max(a, b)
            small = min(a, b)
            return get_greatest_common_divisor(big - small, small)

    gcd = get_greatest_common_divisor(a, b)
    ma = a // gcd
    mb = b // gcd

    times = min(A // ma, B // mb)
    print(str(times * ma)+" "+str(times * mb))
    # return (times * ma, times * mb)
    pass


def main(get_input=input):
    A, B, a, b = map(int, get_input().split())

    (solver(A, B, a, b))
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
