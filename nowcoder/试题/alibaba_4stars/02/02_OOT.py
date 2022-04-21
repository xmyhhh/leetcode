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
class sample:
    def __init__(self, A, B, n):
        self.A = A
        self.B = B
        self.n = n

# 定义处理函数

def solver(A, B, n):


    num_0 = 2
    num_1 = A
    if n == 1:
        return num_1
    if n == 0:
        return num_0
    for i in range(2, n):
        a = num_1
        num_1 = (A * (num_1))% MOD - (B * (num_0))% MOD
        num_0 = a

    return (A * num_1 - B * num_0) % MOD




def main(get_input=input):
    sample_list = []
    N = int(get_input())

    # 处理输入生成测试样例list
    for i in range(N):
        number = list(map(int, get_input().split()))
        sample_list.append(sample(number[0], number[1], number[2]))

    # 逐个处理测试样例
    for item in sample_list:
        print(solver(item.A, item.B, item.n))




if __name__ == '__main__':
    using_input_helper=True
    if using_input_helper:
        inputHelper=InputHelper()
        cProfile.run("main(inputHelper.getInput)")  #test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor