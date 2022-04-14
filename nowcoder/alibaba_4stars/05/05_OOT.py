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
def solver(a, b, n):
    min=0
    detal=list(map(lambda x:abs(x[0]-x[1]),zip(a,b)))
    a,b,detal=zip(*list(sorted(zip(a,b,detal),key=lambda x:x[2],reverse=True)))

    if n<=2:
        return max(sum(a)/2,sum(b)/2)
    for i in range(n-1):
        if a[i]<b[i]:
            min=max(min,a[i]+max(a[i+1:]))
        else:
            min=max(min,b[i]+max(b[i+1:]))
    return min/2
    pass


def main(get_input=input):
    A_list = []
    B_list = []
    N = int(get_input())

    # 处理输入生成测试样例list
    for i in range(N):
        number = list(map(int, get_input().split()))
        A_list.append(number[0])
        B_list.append(number[1])
    # 逐个处理测试样例

    print(solver(A_list,B_list,N))




if __name__ == '__main__':
    using_input_helper = True
    if using_input_helper:
        inputHelper = InputHelper()
        cProfile.run("main(inputHelper.getInput)")  # test with performance monitor
        # main(inputHelper.getInput)  #test without performance monitor
    else:
        # cProfile.run("main()")  #test with performance monitor
        main()  # test without performance monitor
